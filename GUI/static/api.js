//Function for the server of the api
// if we don't put this function the server will close immediatly


    async function getRequest(url='') {
        const response = await fetch(url, {
        method: 'GET', 
        cache: 'no-cache'
        })
        return response.json()
    }

    document.addEventListener('DOMContentLoaded', function() {

    let url = document.location
    let route = "/flaskwebgui-keep-server-alive"
    let interval_request = 3 * 1000 //sec

    function keep_alive_server(){
        getRequest(url + route)
        .then(data => console.log(data))
    }

    setInterval(keep_alive_server, interval_request)

    })

//Validating the data of the interface
    $(function() {
        
        $('a#test').on('click', function(e,arg1,arg2) {
            var arg1 = document.querySelector('#dd1');
            arg1 = arg1.getElementsByTagName('div')[1];
            var arg2 = document.querySelector('#dd2');
            arg2 = arg2.getElementsByTagName('div')[1];
            console.log(arg1.id)
            console.log(arg2.id)

            e.preventDefault()
            if ((arg1.id == 'NULL') || (arg2.id == 'NULL'))
                window.alert('Select an option');
            else{
                $.getJSON('/scraping',{"location":arg1.id , "type":arg2.id},
                    function(data) {
                });
            }
            return false;
        });
        });