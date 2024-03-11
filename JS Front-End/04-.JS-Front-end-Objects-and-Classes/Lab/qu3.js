function convertJSONToObject(text) {
    let objct = JSON.parse(text);
    Object.entries(objct).forEach(([key, value]) => {
        console.log(`${key}: ${value}`);
    })
}

// convertJSONToObject('{"name": "George", "age": 40, "town": "Sofia"}');
// convertJSONToObject('{"name": "Peter", "age": 35, "town": "Plovdiv"}');
