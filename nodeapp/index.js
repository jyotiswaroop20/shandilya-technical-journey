const express = require('express');

const app = express();

app.get("/", (req, res)=> {
    res.json(
        [
            {
                id: 1,
                employeeName: "Onkar Mani Tripathi",
                employeeSalary: 90000
            },
            {
                id: 2,
                employeeName: "Manisha Singh",
                employeeSalary: 60000
            },
            {
                id: 3,
                employeeName: "Priyanka",
                employeeSalary: 10000
            },
            {
                id: 4,
                employeeName: "Jyotiswaroop Tripathi",
                employeeSalary: 75000
            }
        ]
    )
})

app.listen(4000, () => {
    console.log("App is running on Port No: 4000")
})
