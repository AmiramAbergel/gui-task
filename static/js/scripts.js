function displayPath() {
  const fileInput = document.getElementById('file-input');
  const filePath = document.getElementById('file-path');
  if (fileInput.files.length > 0) {
    filePath.value = fileInput.value;
  } else {
    filePath.value = '';
  }
}

function checkAll(){
  fetch('/check-all')
    .then(response => response.text())
    .then(text => {
      const checkboxes = document.querySelectorAll('.tests input[type="checkbox"]');
      checkboxes.forEach(checkbox => checkbox.checked = true);
    });
}

function uncheckAll(){
  fetch('/uncheck-all')
    .then(response => response.text())
    .then(text => {
      const checkboxes = document.querySelectorAll('.tests input[type="checkbox"]');
      checkboxes.forEach(checkbox => checkbox.checked = false);
    });
}

function removeRow(button) {
  const row = button.closest('tr');
  const table = document.querySelector('.users table tbody');
  const index = table.childElementCount - 1;
  fetch(`/remove-row/${index}`)
    .then(response => {
      if (response.status === 204) {
        row.parentNode.removeChild(row);
      }
    });
}

function addRow() {
  const newRow = document.createElement('tr');
  const table = document.querySelector('.users table tbody');
  const index = table.childElementCount;
  const invalidInputs = document.querySelectorAll('.users input:invalid');
  if (invalidInputs.length > 0) {
    invalidInputs[0].focus();
    return;
  }
  fetch(`/add-row/${index}`)
    .then(response => response.text())
      .then(() => {
        newRow.innerHTML = `
            <td><select class="form-control" name="users-${index}-user_type"><option value="admin">Admin</option><option value="standard" selected>Standard</option></select></td>
            <td><input class="form-control" name="users-${index}-email" type="email" required></td>
            <td><input class="form-control" name="users-${index}-password" type="password" required></td>
            <td><button class="btn btn-danger" type="button" onclick="removeRow(this)">Remove</button></td>
        `;

        table.appendChild(newRow);
      });
}

function modifyMessages(message) {
  const messageList = document.querySelector(".alert ul") ;
  const newLi = document.createElement("li");
  newLi.textContent = message;
  messageList.appendChild(newLi);
}