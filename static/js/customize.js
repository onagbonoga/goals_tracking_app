function add(itemName, status,name) 
{
	//console.log("hi")
	//Create an input type dynamically.
	//var goalName = document.createElement("H3");
	//goalName.innerHTML = name;
	console.log(status);
	var element = document.createElement("input");
	var element2 = document.createElement("label");
	var newLine = document.createElement("br");
	element2.innerHTML = itemName;
	

	//Assign different attributes to the element.
	element.setAttribute("type", "checkbox");
	element.setAttribute("value", itemName);
	element.setAttribute("name", itemName);
	element.setAttribute("label", itemName);
	element.setAttribute("id", itemName);
	element2.setAttribute("for",itemName );

	if (status != "false")
	element.setAttribute("checked", true); 

	var foo = document.getElementById("fooBar");

	//Append the element in page (in span).
	//document.getElementById("goalName").appendChild(goalName);
	foo.appendChild(element);
	foo.appendChild(element2);
	foo.appendChild(newLine);

						

	//document.getElementById(fooBar).appendChild(element2);
}

function addName(name)
{
	var goalName = document.createElement("H3");
	goalName.innerHTML = name;
	var foo = document.getElementById("goalName");
	foo.appendChild(goalName);
}

function addTodo(name)
{
	var newGoal = document.createElement("input");
	var newLine = document.createElement("br");
	newGoal.setAttribute("type", "text");
	newGoal.setAttribute("name", "todoItemF");

	var todoSpan = document.getElementById("todoSpan");
	todoSpan.appendChild(newGoal);
	todoSpan.appendChild(newLine);
}