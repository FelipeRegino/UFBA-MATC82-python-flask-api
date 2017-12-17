from flask import Flask, redirect, request, make_response, jsonify
from mongoengine import connect
from task import Task
from bson import json_util

connect(db='sysweb_project', host='ds141406.mlab.com', username='root', password='123mil', port=41406)

app = Flask(__name__)
app.debug = True

@app.route('/api/tasks', methods=['GET'])
def getTasks():
	tasks = json_util.dumps(Task.objects(complete=False, deleted=False).to_json())

	return jsonify({'tasks': tasks});

@app.route('/api/tasks', methods=['POST'])
def createTask():

	title = request.json['title']
	priority = request.json['priority']
	duedate = request.json['duedate']


	task = Task(title=title, priority=priority, duedate=duedate, complete=False, deleted=False)
	task.save()

	return make_response(jsonify({'success': 'task creada'}), 200)

@app.route('/api/tasks/<id>', methods=['DELETE'])
def deleteTask(id):
	Task.objects(pk=id).update_one(deleted=True)

	return make_response(jsonify({'success': 'task deletada'}), 200)

@app.route('/api/tasks/<id>', methods=['PATCH'])
def completeTask(id):
	Task.objects(pk=id).update_one(complete=True)

	return make_response(jsonify({'success': 'task completada'}), 200)

@app.route('/api/tasks/<id>', methods=['PUT'])
def editTask(id):

	title = request.json['title']
	priority = request.json['priority']
	duedate = request.json['duedate']

	Task.objects(pk=id).update_one(title=title, priority=priority, duedate=duedate)

	return make_response(jsonify({'success': 'task atualizada'}), 200)

if __name__ == '__main__':
	port = 8000
	host = '0.0.0.0'
	app.run(port=port, host=host)