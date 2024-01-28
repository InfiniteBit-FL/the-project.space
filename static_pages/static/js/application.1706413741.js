// Manage mobile navigation
document.querySelector('#navopen').addEventListener('click', function() {
    document.querySelector('#mobnav').classList.remove('hidden');
})
document.querySelector('#navclose').addEventListener('click', function() {
    document.querySelector('#mobnav').classList.add('hidden');
})