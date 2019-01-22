var lobnekutil = {
    createLink: function (link) {
        const currentLocation = window.location;
        return currentLocation.origin + link;
    },

    updateLink: function (dom, link) {
        dom.attr("href", lobnekutil.createLink(link)).text(lobnekutil.createLink(link));
    }
};
