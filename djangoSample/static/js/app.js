function validate() {
    var amount = document.getElementById("amount").value;

    if (amount != 1000) {
        alert('You can only create 1000t');
        return false;
    } else {
        return true;
    }
}