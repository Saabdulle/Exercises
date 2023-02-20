function task(newTask) {
    const taskItem = document.createElement('li');
    taskItem.setAttribute('class', 'task-input');
    
    const addNewTask = document.createElement('class');
    addNewTask.setAttribute('class', 'new-task-button')

    const newTaskInfo = document.createElement('span');
    newTaskInfo.setAttribute('class', 'task-info');

    newTaskInfo.appendChild(newTask)

}
task(newTask)
