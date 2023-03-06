// autoexecutable function
// (function(){
//     console.log("hi");
// })();

//function when DOM is loaded
// document.addEventListener('DOMContentLoaded', function () {
//     console.log("bye");
//     const myModal = new bootstrap.Modal('#modal_window', {
//         keyboard: false
//       }).show()
// });


function showModalWindow(){
    const myModal = new bootstrap.Modal('#modal_window', {
        keyboard: false
      }).show()
}

function editTitleWithModalWindow(){
    const content = document.getElementById("page-title");
    const modalContent = document.getElementById("modal-content");
    console.log(content.innerHTML);
    modalContent.innerHTML = content.innerHTML;
    const myModal = new bootstrap.Modal('#modal_window', {
        keyboard: false
      }).show();
}

function updateTitleWithModalWindow(){
    const content = document.getElementById("page-title");
    const modalContent = document.getElementById("modal-content");
    console.log(modalContent.value);
    content.innerHTML = modalContent.value;
}

 