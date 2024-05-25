// scripts.js
new Vue({
    el: '#app',
    data: {
        newTask: '',
        tasks: []
    },
    created() {
        this.fetchTasks();
    },
    methods: {
        async fetchTasks() {
            try {
                const response = await fetch('localhost:8080/tasks');
                const data = await response.json();
                this.tasks = data;
            } catch (error) {
                console.error('获取任务失败:', error);
            }
        },
        async addTask() {
            if (this.newTask.trim() === '') {
                alert('请输入一个任务:');
                return;
            }
            try {
                const response = await fetch('localhost:8080/tasks', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ text: this.newTask })
                });
                const data = await response.json();
                this.tasks.push(data);
                this.newTask = '';
            } catch (error) {
                console.error('添加任务失败:', error);
            }
        },
        async deleteTask(index) {
            const taskId = this.tasks[index]._id;
            try {
                await fetch(`localhost:8080/tasks/${taskId}`, {
                    method: 'DELETE'
                });
                this.tasks.splice(index, 1);
            } catch (error) {
                console.error('删除任务失败:', error);
            }
        },
        toggleTask(index) {
            this.tasks[index].completed = !this.tasks[index].completed;
        },
        editTask(index) {
            this.tasks[index].editing = true;
        },
        async saveEditedTask(index) {
            const editedTask = this.tasks[index];
            if (editedTask.text.trim() === '') {
                alert('Task cannot be empty.');
                return;
            }
            try {
                await fetch(`localhost:8080/tasks/${editedTask._id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(editedTask)
                });
                editedTask.editing = false;
            } catch (error) {
                console.error('编辑任务失败:', error);
            }
        }
    }
});
