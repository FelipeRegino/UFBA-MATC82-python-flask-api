from mongoengine import Document, StringField, DateTimeField, IntField, BooleanField

class Task(Document):
	title = StringField()
	duedate = DateTimeField()
	priority = IntField()
	complete = BooleanField()
	deleted = BooleanField()