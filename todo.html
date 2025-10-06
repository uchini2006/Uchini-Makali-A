<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Advanced To-Do List App</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f9;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      transition: background 0.3s, color 0.3s;
    }
    .dark {
      background: #121212;
      color: white;
    }
    .container {
      background: #fff;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
      width: 420px;
      text-align: center;
      transition: background 0.3s, color 0.3s;
    }
    .dark .container {
      background: #1e1e1e;
      color: white;
    }
    h1 {
      margin-bottom: 10px;
    }
    input, select {
      padding: 8px;
      margin: 5px 0;
      border: 1px solid #ccc;
      border-radius: 6px;
    }
    button {
      padding: 8px 12px;
      margin: 5px;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }
    button:hover {
      background: #0056b3;
    }
    ul {
      list-style: none;
      padding: 0;
      margin-top: 15px;
      max-height: 200px;
      overflow-y: auto;
    }
    li {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #f9f9f9;
      margin: 5px 0;
      padding: 10px;
      border-radius: 6px;
    }
    li.completed span {
      text-decoration: line-through;
      color: gray;
    }
    .priority-high { color: red; }
    .priority-medium { color: orange; }
    .priority-low { color: green; }
    .overdue { background: #ffcccc; }
    .delete {
      background: #dc3545;
      color: white;
      border: none;
      padding: 5px 10px;
      border-radius: 4px;
      cursor: pointer;
    }
    .edit {
      background: #28a745;
      color: white;
      border: none;
      padding: 5px 10px;
      border-radius: 4px;
      cursor: pointer;
      margin-right: 5px;
    }
    .toggle-btn {
      background: #444;
      color: white;
      float: right;
      margin-top: -40px;
      margin-bottom: 10px;
    }
    .search-box {
      width: 100%;
      padding: 8px;
      margin-top: 10px;
      border: 1px solid #ccc;
      border-radius: 6px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>✅ To-Do List</h1>
    <button class="toggle-btn" onclick="toggleDarkMode()">🌙</button>
    <input type="text" id="taskInput" placeholder="Enter task">
    <select id="priority">
      <option value="low">Low Priority</option>
      <option value="medium">Medium Priority</option>
      <option value="high">High Priority</option>
    </select>
    <input type="date" id="dueDate">
    <button onclick="addTask()">Add</button>
    <input type="text" id="search" class="search-box" placeholder="Search tasks..." onkeyup="filterTasks()">
    <ul id="taskList"></ul>
  </div>

  <script>
    window.onload = loadTasks;

    function addTask() {
      let taskInput = document.getElementById("taskInput");
      let priority = document.getElementById("priority").value;
      let dueDate = document.getElementById("dueDate").value;

      if (taskInput.value.trim() === "") return;

      let task = {
        text: taskInput.value,
        priority: priority,
        dueDate: dueDate,
        completed: false
      };

      saveTask(task);
      displayTask(task);

      taskInput.value = "";
      document.getElementById("dueDate").value = "";
    }

    function displayTask(task) {
      let li = document.createElement("li");

      let checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.checked = task.completed;
      checkbox.onchange = function () {
        task.completed = checkbox.checked;
        if (checkbox.checked) li.classList.add("completed");
        else li.classList.remove("completed");
        updateLocalStorage();
      };

      let span = document.createElement("span");
      span.textContent = task.text;
      span.classList.add("priority-" + task.priority);

      if (task.dueDate) {
        let due = new Date(task.dueDate);
        let today = new Date();
        if (due < today && !task.completed) li.classList.add("overdue");
        span.textContent += " (Due: " + task.dueDate + ")";
      }

      // ✏ Edit button
      let editBtn = document.createElement("button");
      editBtn.textContent = "Edit";
      editBtn.className = "edit";
      editBtn.onclick = function () {
        let newText = prompt("Edit task:", task.text);
        if (newText === null || newText.trim() === "") return;

        let newPriority = prompt("Change priority (low, medium, high):", task.priority);
        if (!["low", "medium", "high"].includes(newPriority)) newPriority = task.priority;

        let newDate = prompt("Change due date (YYYY-MM-DD):", task.dueDate);

        task.text = newText.trim();
        task.priority = newPriority;
        task.dueDate = newDate;

        li.remove();
        updateTask(task.text, task); // update by new text
        displayTask(task);
        updateLocalStorage();
      };

      let delBtn = document.createElement("button");
      delBtn.textContent = "Delete";
      delBtn.className = "delete";
      delBtn.onclick = function () {
        li.remove();
        removeTask(task.text);
      };

      li.appendChild(checkbox);
      li.appendChild(span);
      li.appendChild(editBtn);
      li.appendChild(delBtn);

      if (task.completed) li.classList.add("completed");

      document.getElementById("taskList").appendChild(li);
    }

    function filterTasks() {
      let searchValue = document.getElementById("search").value.toLowerCase();
      let tasks = document.getElementById("taskList").getElementsByTagName("li");
      for (let i = 0; i < tasks.length; i++) {
        let text = tasks[i].innerText.toLowerCase();
        tasks[i].style.display = text.includes(searchValue) ? "" : "none";
      }
    }

    function toggleDarkMode() {
      document.body.classList.toggle("dark");
    }

    // Local Storage Functions
    function saveTask(task) {
      let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
      tasks.push(task);
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    function loadTasks() {
      let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
      tasks.forEach(task => displayTask(task));
    }

    function removeTask(text) {
      let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
      tasks = tasks.filter(t => t.text !== text);
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    function updateTask(oldText, updatedTask) {
      let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
      tasks = tasks.map(t => (t.text === oldText ? updatedTask : t));
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    function updateLocalStorage() {
      let tasks = [];
      document.querySelectorAll("#taskList li").forEach(li => {
        let checkbox = li.querySelector("input[type='checkbox']");
        let span = li.querySelector("span");
        let taskText = span.textContent.split(" (Due:")[0];
        let priorityClass = span.className.split("-")[1];
        let dueDateMatch = span.textContent.match(/\(Due: (.*?)\)/);
        let dueDate = dueDateMatch ? dueDateMatch[1] : "";

        tasks.push({
          text: taskText,
          priority: priorityClass,
          dueDate: dueDate,
          completed: checkbox.checked
        });
      });
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }
  </script>
</body>
</html>
