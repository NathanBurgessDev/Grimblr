export default class APIService {
    

    static InsertName(name) {
        return fetch("http://localhost:5000/result", {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body:JSON.stringify(name)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}