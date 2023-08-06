import os
import logging
import uuid
from pathlib import Path
from typing import List

from rdflib import Graph, OWL, RDF, RDFS
from rdflib.query import Result, ResultRow

from drb.topics.dao.topic_dao import DrbTopicDao
from drb.core.signature import parse_signature
from drb.topics.topic import DrbTopic, TopicCategory
from drb.exceptions.core import DrbException

logger = logging.getLogger('DrbTopic')


class RDFDao(DrbTopicDao):

    __triple = {'.owl': 'application/rdf+xml', '.ttl': 'turtle'}

    def __init__(self, path: str):
        # if not existing, generate a new file.
        Path(path).touch(exist_ok=True)
        self.__file = path
        self.__format = self.__triple[os.path.splitext(path)[1]]
        self.__result = self.__query_rdf_file()

    def __query_rdf_file(self) -> Result:
        """
        Search for all topics in an RDF supported resource.
        Returns:
            SPARQLResult: list containing found topics
        """

        path = os.path.join(self.__file)
        g = Graph()
        g.parse(source=path, format=self.__format)
        result = g.query("""
                SELECT ?Class ?label ?id ?category ?factory
                (GROUP_CONCAT(DISTINCT IF(BOUND(?parentClassId),
                STR(?parentClassId),
                ?parentClass); separator="§ ") AS ?parentClasses)
                (GROUP_CONCAT(DISTINCT IF(BOUND(?nameMatch), ?nameMatch, "");
                separator="§ ") AS ?nameMatches)
                (GROUP_CONCAT(DISTINCT IF(BOUND(?xqueryTest), ?xqueryTest, "");
                separator="§ ") AS ?xqueryTests)
                WHERE {
                ?Class a owl:Class .
                ?Class rdfs:label ?label .
                OPTIONAL { ?Class drb:id ?id .}
                OPTIONAL { ?Class drb:category ?category .}
                OPTIONAL { ?Class drb:implementationIdentifier ?factory .}
                OPTIONAL {
                ?Class rdfs:subClassOf ?parentClass .
                OPTIONAL { ?parentClass drb:id ?parentClassId .}
                }
                OPTIONAL { ?Class drb:signature/drb:nameMatch ?nameMatch . }
                OPTIONAL { ?Class drb:signature/drb:xqueryTest ?xqueryTest . }
                }
                GROUP BY ?Class ?label ?id ?category ?factory
                """)

        return result

    def __generate_topic_from_rdf(self, row: ResultRow) -> DrbTopic:
        """
        Converts a row into a dictionary used for generating RDFTopic(s).
        Parameters:
            row (ResultRow): row to convert
        Returns:
            DrbTopic: the corresponding topic
        """
        data = {}
        uri_parents = str(row.parentClasses).split("§ ") if str(
            row.parentClasses) else None

        name_signatures = str(row.nameMatches).split("§ ") if str(
            row.nameMatches) else None
        xquery_signatures = str(row.xqueryTests).split("§ ") if str(
            row.xqueryTests) else None

        data['uri'] = row.Class.toPython()
        data['label'] = row.label.toPython()
        if row.id is not None:
            data['id'] = uuid.UUID(row.id.toPython())
        else:
            data['id'] = self.generate_id(data['uri'])
        if row.category is not None:
            data['category'] = TopicCategory(row.category.toPython())
        else:
            data['category'] = TopicCategory('CONTAINER')
        if row.factory is not None:
            data['factory'] = row.factory.toPython()

        parents = []
        if uri_parents is not None:
            for uri_parent in uri_parents:
                try:
                    parents.append(uuid.UUID(uri_parent))
                except ValueError:
                    parents.append(self.generate_id(uri_parent))
            data['subClassOf'] = parents

        signatures = []
        if name_signatures is not None:
            for n_signature in name_signatures:
                signatures.append({'name': n_signature})

        if xquery_signatures is not None:
            for x_signature in xquery_signatures:
                signatures.append({'xquery': x_signature})

        data['signatures'] = [parse_signature(s) for s in signatures]

        topic = DrbTopic(**data)
        return topic

    @staticmethod
    def generate_id(uri: str) -> uuid.UUID:
        """
        Generates an unique UUID from topic's unique URI.
        Parameters:
            uri (str): topic's unique URI
        Returns:
            UUID: topic's unique
        """
        return uuid.uuid3(uuid.NAMESPACE_DNS, uri)

    def read(self, identifier: uuid.UUID) -> DrbTopic:
        """
        Reads a topic from an RDF file.
        Parameters:
            identifier (UUID): id of topic to read from file
        Returns:
            DrbTopic: the topic corresponding to the given identifier
                """

        for r in self.__result:
            if r.id is not None:

                if uuid.UUID(r.id.toPython()) == identifier:
                    topic = self.__generate_topic_from_rdf(r)
                    return topic
            else:
                uri = r.Class.toPython()
                id_from_uri = self.generate_id(uri)
                if id_from_uri == identifier:
                    topic = self.__generate_topic_from_rdf(r)
                    return topic

            continue

        raise DrbException

    def find(self, search: str) -> List[DrbTopic]:
        """
        Finds a topic from an RDF file.
        Parameters:
            search (str): label of topic to read from file
        Returns:
            List[DrbTopic]: the topic corresponding to the given label
        """
        topics = []
        for r in self.__result:
            if search in r.label.toPython():
                topic = self.__generate_topic_from_rdf(r)
                topics.append(topic)

        return topics

    def read_all(self) -> List[DrbTopic]:
        """
        Loads all topics defined in RDF files.
        """

        topics = []

        for r in self.__result:

            try:
                topic = self.__generate_topic_from_rdf(r)
                topics.append(topic)

            except TypeError:
                continue

        return topics

    def create(self, topic: DrbTopic) -> DrbTopic:
        raise NotImplementedError

    def update(self, topic: DrbTopic) -> DrbTopic:
        raise NotImplementedError

    def delete(self, identifier: uuid.UUID) -> None:
        raise NotImplementedError
