const newTaskInput = document.getElementById('newTaskInput')
const todoList = document.getElementById('todo-list')
const taskButton = document.getElementById('task-button')



function task(newTask) {
    const taskItem = document.createElement('li');
    taskItem.setAttribute('class', 'task-input');
    
    const addNewTask = document.createElement('div');
    addNewTask.setAttribute('class', 'new-task-button')


    const newTaskInfo = document.createElement('span');
    newTaskInfo.setAttribute('class', 'task-info');

    newTaskInfo.innerText = newTask;

    todoList.appendChild(taskItem)

    taskItem.appendChild(taskButton)

    taskItem.appendChild(newTaskInfo)

}

