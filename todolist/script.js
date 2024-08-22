document.addEventListener("DOMContentLoaded", function() {
    const taskinput = document.getElementById("task-input");
    const addtaskbtn = document.getElementById("add-task-btn");
    const tasklist = document.getElementById("task-list");
    const prioritySelect = document.getElementById("priority-select");

    loadTasks();

    addtaskbtn.addEventListener("click", function() {
        const tasktext = taskinput.value.trim();
        const priority = prioritySelect.value;
        if (tasktext !== "") {
            addTask(tasktext, priority);
            taskinput.value = "";
            saveTasks();
        }
    });

    taskinput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            const tasktext = taskinput.value.trim();
            const priority = prioritySelect.value;
            if (tasktext !== "") {
                addTask(tasktext, priority);
                taskinput.value = "";
                saveTasks();
            }
        }
    });

    function addTask(tasktext, priority) {
        const li = document.createElement("li");
        li.className = `task ${priority}`;

        const span = document.createElement("span");
        span.textContent = tasktext;

        const deletebtn = document.createElement("button");
        deletebtn.textContent = "Delete";
        deletebtn.addEventListener("click", function() {
            li.remove();
            saveTasks();
        });

        span.addEventListener("click", function() {
            li.classList.toggle("completed");
            saveTasks();
        });

        li.appendChild(span);
        li.appendChild(deletebtn);
        tasklist.appendChild(li);
    }

    function saveTasks() {
        const tasks = [];
        tasklist.querySelectorAll("li").forEach(function(li) {
            const task = {
                text: li.querySelector("span").textContent,
                priority: li.classList.contains("high") ? "high" :
                          li.classList.contains("medium") ? "medium" : "low",
                completed: li.classList.contains("completed")
            };
            tasks.push(task);
        });
        localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    function loadTasks() {
        const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
        tasks.forEach(function(task) {
            addTask(task.text, task.priority);
            if (task.completed) {
                tasklist.lastChild.classList.add("completed");
            }
        });
    }
});
