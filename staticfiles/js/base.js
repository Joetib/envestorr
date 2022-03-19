
function construct_url(key, value, exclude) {
    var url_list = window.location.href.split('?');
    var url = url_list[0] + '?'
    if (url_list.length > 1) {
        var queries = url_list[1];
        queries.split('&').forEach(function (i) {
            let left = i.split("=")[0]
            if (i.length !== 0 && left !== key && left !== exclude) {
                url += i + '&'
            }
        });
    }
    url += key + '=' + value;
    window.location.replace(url);
    return False;
}
function like_handler(e) {
    e.preventDefault();
    console.log("like handler called");
    console.log(this);
    url = this.dataset.url;
    target = document.querySelector(this.dataset.target);
    
    if (this.dataset.liked == 1){
         url = url+ "?unlike=1"
    }
    console.log(url)
    fetch(url).then(e => e.json()).then(
        (data) => {
            if (data.liked) {
                this.classList.add('text-warning');
                this.dataset['liked'] = 1;

            } else {
                this.classList.remove('text-warning');
                this.dataset['liked'] = 0;
            }
            target.innerText = data['likes_count'];
        });



}
(() => {
    let sidebar = document.getElementById('navbarSupportedContent');
    function toggleSidebar() {
        sidebar.classList.toggle('show');
    }
    document.getElementById('sidebar-toggle').addEventListener('click', toggleSidebar);

}
)();
(() => {
    console.log("running");
    let items = document.getElementsByClassName('like_button');
    for (let item of items) {
        item.addEventListener('click', like_handler)
    }
})();
(() => {
    document.getElementById("search_form").addEventListener('submit', function (e) {
        e.preventDefault();
        let input = document.getElementById("article-search");
        construct_url(
            "search",
            input.value,
            null
        );
    });

})();
