function gallery_browser_init(field_name, url, type, win) {
    console.log('In gallery browsr init');
    tinyMCE.activeEditor.windowManager.open({
        url: "/gallery/browser/",
        width: 800,
        height: 600,
        movable: true,
        inline: true,
        close_previous: "no"
    }, {
        window : win,
        input : field_name
    });  
}
