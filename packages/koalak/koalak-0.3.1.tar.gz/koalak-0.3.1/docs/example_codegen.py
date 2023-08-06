from koalak.relationaldb import BaseMongodbDatabase, BaseObjects


class BaseDatabase(BaseMongodbDatabase):
    def __init__(
        self,
        dbname: str,
        host: str = "127.0.0.1",
        port: int = 27017,
        timeout: int = 300,
        username: str = None,
        password: str = None,
    ):
        BaseMongodbDatabase.__init__(
            self, dbname, host, port, timeout, username, password
        )

        self.persons = PersonObjects(self)

        self.Person = self.persons

        self.animals = AnimalObjects(self)

        self.Animal = self.animals


class PersonObjects(BaseObjects):
    collection_name = "persons"

    # ====== #
    # CREATE #
    # ====== #
    def insert_one(self, firstname: str, *, lastname: str, birth_year: int):
        query = {
            "firstname": firstname,
            "lastname": lastname,
            "birth_year": birth_year,
        }
        self.collection.insert_one(query)

    new = insert_one

    # ==== #
    # READ #
    # ==== #
    def find_asdict(
        self, firstname: str = None, *, lastname: str = None, birth_year: int = None
    ):
        query = {}

        if firstname is not None:
            query["firstname"] = firstname

        if lastname is not None:
            query["lastname"] = lastname

        if birth_year is not None:
            query["birth_year"] = birth_year

        return self.collection.find(query)

    def detailed_find_asdict(
        self,
        firstname: str = None,
        *,
        lastname: str = None,
        birth_year: int = None,
        skip=None,
        limit=None,
        fields=None,
    ):
        pipeline = []

        match_pipeline = {"$match": {"$and": []}}
        and_match_pipeline = match_pipeline["$match"]["$and"]

        if firstname is not None:
            and_match_pipeline.append({"firstname": firstname})

        if lastname is not None:
            and_match_pipeline.append({"lastname": lastname})

        if birth_year is not None:
            and_match_pipeline.append({"birth_year": birth_year})

        if and_match_pipeline:
            pipeline.append(match_pipeline)

        pipeline.extend([])

        if skip:
            pipeline.append({"$skip": skip})
        if limit:
            pipeline.append({"$limit": limit})

        if fields:
            pipeline.append({"$project": {field: 1 for field in fields}})

        return self.collection.aggregate(pipeline)

    def light_find_asdict(
        self,
        firstname: str = None,
        *,
        lastname: str = None,
        birth_year: int = None,
        skip=None,
        limit=None,
        fields=None,
    ):
        objects = self.detailed_find_asdict(
            skip=skip,
            limit=limit,
            fields=fields,
            firstname=firstname,
            lastname=lastname,
            birth_year=birth_year,
        )

        yield from objects

    def first_asdict(
        self, firstname: str = None, *, lastname: str = None, birth_year: int = None
    ):
        query = {}

        if firstname is not None:
            query["firstname"] = firstname

        if lastname is not None:
            query["lastname"] = lastname

        if birth_year is not None:
            query["birth_year"] = birth_year

        return self.collection.find_one(query)

    def first(
        self, firstname: str = None, *, lastname: str = None, birth_year: int = None
    ):
        document = self.first_asdict(
            firstname=firstname,
            lastname=lastname,
            birth_year=birth_year,
        )
        return self.from_dict(document)

    def find(
        self, firstname: str = None, *, lastname: str = None, birth_year: int = None
    ):
        documents = self.find_asdict(
            firstname=firstname,
            lastname=lastname,
            birth_year=birth_year,
        )
        for document in documents:
            yield self.from_dict(document)

    def feed(
        self, firstname: str, *, lastname: str, birth_year: int, _retid: bool = False
    ):
        raise ValueError(
            f"This entity {self.entity.name!r} can not use the method 'feed' "
            f"as it doesn't have any in_filter_query_attribute"
        )

    # ====== #
    # DELETE #
    # ====== #
    def delete_first(
        self, firstname: str = None, *, lastname: str = None, birth_year: int = None
    ):
        query = {}

        if firstname is not None:
            query["firstname"] = firstname

        if lastname is not None:
            query["lastname"] = lastname

        if birth_year is not None:
            query["birth_year"] = birth_year

        self.collection.delete_one(query)

    delete_one = delete_first

    def delete_many(
        self, firstname: str = None, *, lastname: str = None, birth_year: int = None
    ):
        query = {}

        if firstname is not None:
            query["firstname"] = firstname

        if lastname is not None:
            query["lastname"] = lastname

        if birth_year is not None:
            query["birth_year"] = birth_year

        self.collection.delete_many(query)

    # ===== #
    # UTILS #
    # ===== #
    def _normalize(self, obj):
        if isinstance(obj, tuple):
            return obj, {}

        else:
            raise ValueError("can not normalize object")

    def _feed_and_get_id(self, obj):
        if isinstance(obj, Person):
            return obj.id
        args, kwargs = self._normalize(obj)
        return self.feed(*args, **kwargs, _retid=True)


class AnimalObjects(BaseObjects):
    collection_name = "animals"

    # ====== #
    # CREATE #
    # ====== #
    def insert_one(self, name: str, person: Person):
        if not isinstance(person, Person):
            raise TypeError("Only Person objects are accepted for insertion")
        person = person.id

        query = {
            "name": name,
            "person": person,
        }
        self.collection.insert_one(query)

    new = insert_one

    # ==== #
    # READ #
    # ==== #
    def find_asdict(self, name: str = None, person: Person = None):
        query = {}

        if name is not None:
            query["name"] = name

        if person is not None:
            query["person"] = person

        return self.collection.find(query)

    def detailed_find_asdict(
        self,
        name: str = None,
        person: Person = None,
        skip=None,
        limit=None,
        fields=None,
    ):
        pipeline = []

        match_pipeline = {"$match": {"$and": []}}
        and_match_pipeline = match_pipeline["$match"]["$and"]

        if name is not None:
            and_match_pipeline.append({"name": name})

        if person is not None:
            and_match_pipeline.append({"person": person})

        if and_match_pipeline:
            pipeline.append(match_pipeline)

        pipeline.extend(
            [
                {
                    "$lookup": {
                        "from": "Person",
                        "localField": "person",
                        "foreignField": "_id",
                        "as": "person",
                    }
                },
                {"$set": {"person": {"$arrayElemAt": ["$person", 0]}}},
                {"$project": {"person._id": 0}},
            ]
        )

        if skip:
            pipeline.append({"$skip": skip})
        if limit:
            pipeline.append({"$limit": limit})

        if fields:
            pipeline.append({"$project": {field: 1 for field in fields}})

        return self.collection.aggregate(pipeline)

    def light_find_asdict(
        self,
        name: str = None,
        person: Person = None,
        skip=None,
        limit=None,
        fields=None,
    ):
        objects = self.detailed_find_asdict(
            skip=skip,
            limit=limit,
            fields=fields,
            name=name,
            person=person,
        )

        yield from objects

    def first_asdict(self, name: str = None, person: Person = None):
        query = {}

        if name is not None:
            query["name"] = name

        if person is not None:
            query["person"] = person

        return self.collection.find_one(query)

    def first(self, name: str = None, person: Person = None):
        document = self.first_asdict(
            name=name,
            person=person,
        )
        return self.from_dict(document)

    def find(self, name: str = None, person: Person = None):
        documents = self.find_asdict(
            name=name,
            person=person,
        )
        for document in documents:
            yield self.from_dict(document)

    def feed(self, name: str, person: Person, _retid: bool = False):
        raise ValueError(
            f"This entity {self.entity.name!r} can not use the method 'feed' "
            f"as it doesn't have any in_filter_query_attribute"
        )

    # ====== #
    # DELETE #
    # ====== #
    def delete_first(self, name: str = None, person: Person = None):
        query = {}

        if name is not None:
            query["name"] = name

        if person is not None:
            query["person"] = person

        self.collection.delete_one(query)

    delete_one = delete_first

    def delete_many(self, name: str = None, person: Person = None):
        query = {}

        if name is not None:
            query["name"] = name

        if person is not None:
            query["person"] = person

        self.collection.delete_many(query)

    # ===== #
    # UTILS #
    # ===== #
    def _normalize(self, obj):
        if isinstance(obj, tuple):
            return obj, {}

        else:
            raise ValueError("can not normalize object")

    def _feed_and_get_id(self, obj):
        if isinstance(obj, Animal):
            return obj.id
        args, kwargs = self._normalize(obj)
        return self.feed(*args, **kwargs, _retid=True)
