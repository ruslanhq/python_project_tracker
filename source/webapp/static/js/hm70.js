

function login() {
    $.ajax({
        url: 'http://localhost:8000/api/login/',
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        method: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){localStorage.setItem('apiToken', response.token);},
        error: function(response, status){console.log(response);}
    });}



function projectList() {
    $.ajax({
        url: 'http://localhost:8000/api/projects/',
        method: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });}

function taskList() {
    $.ajax({
        url: 'http://localhost:8000/api/tasks/',
        method: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });}

function taskForProject() {
    $.ajax({
        url: 'http://localhost:8000/api/projects/1/',
        method: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response.projects);},
        error: function(response, status){console.log(response);}
    });}

function createTask() {
    $.ajax({
        url: "http://localhost:8000/api/tasks/",
        method: 'POST',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({summary: 'test', description: 'test_desc', status: 1, type: 1, project: 1}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}

function deleteTask() {
    $.ajax({
        url: "http://localhost:8000/api/tasks/15",
        method: 'DELETE',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}



$(document).ready(function() {
    login();
    projectList();
    taskList();
    taskForProject();
    createTask();
    deleteTask();
});
