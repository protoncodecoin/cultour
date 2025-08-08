const BASEURL = location.host;
let dateElement = document.querySelector(".date__field");
let timeElement = document.querySelector(".time__field");
let noteElement = document.querySelector(".note__field");
let guestsElement = document.querySelector(".guests__field");
let saveReservationBtn = document.querySelector(".save__btn");
let modalElement = document.querySelector(".modal"); // ✅ define modal element

let reservationTableEl = document.querySelector(".reservation__tables");
let secondModal = document.querySelector("#hiddenBookBtn");

let {email } = userEmail;

let csrftoken = getCookie("csrftoken");

let finalTableId = null;

reservationTableEl.addEventListener("click", async function(e){
    const target = e.target
    console.log(target)
    console.log(target.classList.contains("tableID"))
    if (target.classList.contains("tableID")) {
        
        finalTableId= target.dataset.tableId;
    }
});



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function createTableReservation(tableId) {

    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            reservation_date: dateElement.value,
            reservation_time: timeElement.value,
            notes: noteElement.value,
            guests: guestsElement.value,
            table: tableId,
        }),
    }

    const URL = `/api/create-reservation/`;


    try {
        const response = await fetch(URL, options);

        if (!response.ok) {
            throw new Error("Failed to book reservation");
        }

        const respData = await response.json();
        console.log(respData, email, "============ response");

        payWithPaystack(respData["ref"], respData["amount"], respData["object_id"], respData["content_type"])

        // ✅ Close the modal the Bootstrap 5 way
        document.querySelector(".first-close-btn").click();

        // TODO: Fix response modal not showing
        // show second modal
        // secondModal.click();
        document.getElementById("hiddenBookButton").click();


    } catch (error) {

        document.querySelector(".first-close-btn").click();

        document.getElementById("hiddenBookButton").click();
    }
}

saveReservationBtn.addEventListener("click", function(e){

    console.log(finalTableId);

    createTableReservation(finalTableId);
})

console.log("worked !!!!")


function payWithPaystack(ref, amount, table, content_type) {
    let currency = "GHS";
    let plan = "";

    console.log("======== called pay ===============", ref, amount, table, content_type,email)

    let obj = {
        key: "pk_test_17f45c77fbf0880f64302e5ac67425741af647fa",
        amount,
        ref,
        email,
        callback: function(response) {
            // call verify function
            verifyPayment(ref, content_type, table)
        },
    };

    if (Boolean(currency)) {
        obj.currency = currency;
    }else {
        console.log("======= currency ============");
    }

    if (Boolean(plan)) {
        obj.plan - plan;
        console.log("======= plan ============");

    }

    var handler = PaystackPop.setup(obj);
    handler.openIframe();
    
}


async function verifyPayment(ref, content_type, obj_id) {

    console.log("===== called verify ===========");

    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            ref,
            content_type,
            object_id: obj_id,
        }),
    };

    const URL = `/api/payment/verify/`;

    try {
        
        const response = await fetch(URL, options);

        if (!response.ok) {
            console.log(response.statusText);
            throw new Error("Failed to verify transaction")
        }

        const jsonData = await response.json();

        return jsonData;
    } catch (error) {
        console.log(error)
    }

}