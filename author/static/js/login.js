document.getElementById("clickclose").addEventListener("click", function () {
    document.getElementById("divclose").style.visibility = 'hidden'
})
value = document.getElementById("msg_code").innerHTML
if (value == 0) {
    // console.log('hwllo')
    document.getElementById("divclose").style.visibility = 'hidden'
} else {
    // console.log("hellow")
    document.getElementById("divclose").style.visibility = 'show'
}
