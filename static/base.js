function load_urls() {
    toggle_loader(true)
    axios.get('/load_urls/').then((response) => {
        urls = response.data;
        fill_table();
        toggle_loader(false)
    })
}

function update_status() {
    toggle_loader(true)
    axios.get('/update_status/').then((response) => {
        load_urls();
    })
}

function fill_table() {
    let tbody = document.getElementById('table_body');
    tbody.innerHTML = "";
    for (let i = 0; i < urls.length; i++) {
        let row = urls[i]
        let tr = document.createElement('tr')
        let td1 = document.createElement('td');
        let td2 = document.createElement('td');
        let td3 = document.createElement('td');
        td1.innerHTML = row.id
        td2.innerHTML = row.url
        td3.innerHTML = row.status_code
        td3.classList.add("tag")
        td3.classList.add("is-medium")
        td3.classList.add("is-light")
        if (row.status_code == null || row.status_code == "") {
            td3.classList.add("is-light")
            td3.innerHTML = "-"
        } else if (row.status_code !== 200) {
            td3.classList.add("is-danger")
        } else {
            td3.classList.add("is-success")
        }
        tr.appendChild(td1)
        tr.appendChild(td2)
        tr.appendChild(td3)
        tbody.appendChild(tr)
    }
}

function toggle_loader(val) {
    check_status_btn = document.getElementById('check_status');
    if (val === true) {
        if (check_status_btn.classList.contains('is-loading') === false) {
            check_status_btn.classList.add('is-loading')
        }
    } else {
        check_status_btn.classList.remove('is-loading')
    }
}

window.addEventListener("DOMContentLoaded", function () {
    load_urls();
}, false);
