from faker import Faker
from faker.providers import user_agent
import requests

BASEURL = 'https://todo.pixegami.io'

fake = Faker()
fake.add_provider(user_agent)


def new_task_payload(user_id=fake.user_name()):
    return {'content': fake.sentence(),
            'user_id': user_id,
            'is_done': False}


def create_new_task(todo_payload):
    return requests.put(BASEURL + '/create-task', json=todo_payload)


def update_task(updated_payload):
    return requests.put(BASEURL + '/update-task', json=updated_payload)


def get_task(todo_task_id):
    return requests.get(BASEURL + f'/get-task/{todo_task_id}')


def get_tasks_list(user_id):
    return requests.get(BASEURL + f'/list-tasks/{user_id}')


def delete_task(todo_task_id):
    return requests.delete(BASEURL + f'/delete-task/{todo_task_id}')


def test_create_task():
    task_payload = new_task_payload()
    new_task_response = create_new_task(task_payload)
    task_data = new_task_response.json()

    assert new_task_response.status_code == 200
    assert task_data['task']['task_id'] is not None
    assert task_data['task']['content'] == task_payload['content']
    assert task_data['task']['user_id'] == task_payload['user_id']


def test_get_task():
    # creating a task
    task_payload = new_task_payload()
    new_task_response = create_new_task(task_payload)
    task_data = new_task_response.json()
    task_id = task_data['task']['task_id']
    assert task_id is not None

    # getting a task
    get_todo_task_response = get_task(task_id)
    assert get_todo_task_response.status_code == 200
    assert task_data['task']['content'] == task_payload['content']
    assert task_data['task']['user_id'] == task_payload['user_id']


def test_update_task():
    # create new task
    task_payload = new_task_payload()
    new_task_response = create_new_task(task_payload)
    assert new_task_response.status_code == 200
    task_data = new_task_response.json()['task']
    task_id = task_data['task_id']
    assert task_id is not None

    # update the task
    updated_payload = {
        'user_id': task_payload['user_id'],
        'task_id': task_id,
        'content': 'new new new updated content',
        'is_done': True
    }
    update_task_response = update_task(updated_payload)
    assert update_task_response.status_code == 200

    # checking the updated task
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    updated_task_data = get_task_response.json()
    assert updated_task_data['content'] == updated_payload['content']
    assert updated_task_data['is_done'] == updated_payload['is_done']


def test_get_tasks_list():
    # creating tasks for the same user
    user_id = fake.user_name()
    tasks_number = 3
    for _ in range(tasks_number):

        task_payload = new_task_payload(user_id=user_id)
        new_task_response = create_new_task(task_payload)
        assert new_task_response.status_code == 200

    # checking user tasks list
    tasks_list_response = get_tasks_list(user_id)
    assert tasks_list_response.status_code == 200
    tasks = tasks_list_response.json()['tasks']
    assert len(tasks) == tasks_number


def test_delete_task():
    # creating a task
    task_payload = new_task_payload()
    new_task_response = create_new_task(task_payload)
    task_data = new_task_response.json()
    task_id = task_data['task']['task_id']
    assert task_id is not None

    # deleting a task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    delete_data = delete_task_response.json()
    assert delete_data['deleted_task_id'] == task_id

    # checking the task is not there anymore
    getting_deleted_task_response = get_task(task_id)
    assert getting_deleted_task_response.status_code == 404
