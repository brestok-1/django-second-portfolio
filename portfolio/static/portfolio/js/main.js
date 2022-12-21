// window.onload = () => {
//     let dropdownItems = document.getElementsByClassName('f')
//     for (let item of dropdownItems) {
//         item.addEventListener('click', (() => {
//             let isActive = false;
//             return function() {
//                 isActive = !isActive;
//                 isActive ? item.classList.add('active') : item.classList.remove('active')
//             }
//         })())
//         item.addEventListener('mouseenter', function(){
//             item.classList.add('contact-hover')
//         })
//         item.addEventListener('mouseleave', function(){
//             item.classList.remove('contact-hover')
//         })
//     }
// }