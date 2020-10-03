function add(name,data,priority) 
{
	//console.log("hi")
	//Create an input type dynamically.
	var goalName = document.createElement("H3");
	goalName.innerHTML = name;
	data = JSON.parse(data);
	console.log(typeof(data['eat it']));
	var foo = document.getElementById(priority);
	foo.appendChild(goalName);

	for (const itemName in data)
	{
		var element = document.createElement("input");
		var element2 = document.createElement("label");
		var newLine = document.createElement("br");
		element2.innerHTML = itemName;
		

		//Assign different attributes to the element.
		element.setAttribute("type", "checkbox");
		element.setAttribute("value", itemName);
		element.setAttribute("name", itemName);
		//element.setAttribute("label", itemName);
		element.setAttribute("id", itemName);
		element2.setAttribute("for",itemName );

		if (data[itemName] == true)
		element.setAttribute("checked", true); 
	
		foo.appendChild(element);
		foo.appendChild(element2);
		foo.appendChild(newLine);
	}
	//Append the element in page (in span).

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