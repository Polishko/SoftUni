from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self) -> None:
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> Category.edit:
        current_category = [c for c in self.categories if c.id == category_id][0]

        if current_category:
            return current_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> Topic.edit:
        current_topic = [t for t in self.topics if t.id == topic_id][0]

        if current_topic:
            return current_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> Document.edit:
        current_document = [d for d in self.documents if d.id == document_id][0]

        if current_document:
            return current_document.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        current_category = [c for c in self.categories if c.id == category_id][0]

        if current_category:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id) -> None:
        current_topic = [t for t in self.topics if t.id == topic_id][0]

        if current_topic:
            self.topics.remove(current_topic)

    def delete_document(self, document_id) -> None:
        current_document = [d for d in self.documents if d.id == document_id][0]

        if current_document:
            self.documents.remove(current_document)

    def get_document(self, document_id) -> "Document" or None:
        current_document = [d for d in self.documents if d.id == document_id][0]

        if current_document:
            return current_document

    def __repr__(self) -> str:
        result = [f"{d.__repr__()}" for d in self.documents]
        return "\n".join(result)






