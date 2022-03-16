
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
(() => {
    document.getElementById("search_form").addEventListener('submit', function(e){
        e.preventDefault();
        let input = document.getElementById("article-search");
        construct_url(
            "search",
            input.value,
            null
        );
    });

})();