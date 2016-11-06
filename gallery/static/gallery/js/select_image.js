function formatState (state) {
    if (!state.id) { return state.text; }

    var url = state.text.substr(0, state.text.search(':'));
    var name = state.text.substr(state.text.search(':')+1);
    var $state = $(
        '<span><img src="' + url + '" width="100" /> ' + name + '</span>'
    );
    return $state;
};

$(document).ready(function() {
    console.log('wee');
    $(".image_select").click(function() {
        console.log('hmm');
    });
    $(".image_select").select2({
        templateResult: formatState
    });
});
