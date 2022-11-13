// let parseResponse = (response) => {
//   return response.json().then((json => {
//     if (!response.ok) {
//       return Promise.reject(json);
//     }
//     console.log(json)
//     return json
//   }))
// }

export async function InsertName(name) {
    return fetch("http://localhost:5000/result", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(name)
    })
}
// export function InsertName(name) {
//     const [response, setResponse] = useState([]);
//     const [loading, setLoading] = useState([])

//     useEffect(() => {
//         setLoading(true);
//         fetch("http://localhost:5000/result", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(name)
//         })
//         .then(response => console.log(response.json()))
//         .then(responseJson => {
//             setResponse(responseJson);
//             setLoading(false);
//         })
//         .catch(error => console.log(error))
//         setLoading(false);
//     }, []);
    
//     return { loading, response };
// }