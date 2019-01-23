lobnektable = {
    initColumns: function (columns, rend) {
        var cols = [];

        $.each(columns, function (i, val) {
            cols.push({"data": val, "render": rend(val), "defaultContent": "", "title": val});
        });

        return cols;
    },

    columns: function (fields) {
        var cols = [];
        $.each(fields, function (i, val) {
            cols.push(val.name);
        });
        return cols;
    },

    table: function(dom, frame, render) {
        console.log(frame);
        console.log(dom);
        columns = lobnektable.columns(frame.schema.fields);
        datarows = frame.data;

        console.log(columns);
        console.log(datarows);

        return $(dom).dataTable({
            data: frame.data,
            columns: lobnektable.initColumns(columns, render),
            scrollX: false,
            paging: false
        })
    },
}

lobnekgraph = {
    rangeselector: {
        buttons: [
            {type: 'ytd', text: 'YTD'},
            {type: 'year', count: 1, text: '1y'},
            {type: 'year', count: 2, text: '2y'},
            {type: 'year', count: 3, text: '3y'},
            {type: 'year', count: 4, text: '4y'},
            {type: 'year', count: 5, text: '5y'},
            {type: 'year', count: 6, text: '6y'},
            {type: 'year', count: 10, text: '10y'},
            {type: 'all', text: 'All'}
        ],
        selected: 8
    }
};