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
    const modalContent = document.getElementById("modal-content_text_area");
    modalContent.value = '';
    const myModal = new bootstrap.Modal('#modal_window', {
        keyboard: false
      }).show()
}

function editTitleWithModalWindow(){
    const modalContent = document.getElementById("modal-content_text_area");
    modalContent.value = '';
    const content = document.getElementById("page-title");
    console.log(content.innerHTML);
    modalContent.innerHTML = content.innerHTML;
    const myModal = new bootstrap.Modal('#modal_window', {
        keyboard: false
      }).show();
}

function updateTitleWithModalWindow(){
    const content = document.getElementById("page-title");
    const modalContent = document.getElementById("modal-content_text_area");
    console.log(modalContent.value);
    content.innerHTML = modalContent.value;
}

function toggle_like(val) {
    const like_btn = document.getElementById("like_btn");
    const dislike_btn = document.getElementById("dislike_btn");
    
    if (val ==1 ) {
        like_btn.style.display = "block";
        dislike_btn.style.display = "none";
    }
    else {
        like_btn.style.display = "none";
        dislike_btn.style.display = "block";
    }
}

 