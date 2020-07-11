const performance = {
    parse: function (x) {
        rows = [];
        for (var key in x) {
            rows.push({"name": key, "value": x[key]});
        }
        return rows;
    },

    truncate: function (s) {
        var n = s.xData.length;
        var pairs = [];

        for (i = 0; i < n; i++) {
            if (s.xData[i] >= s.xAxis.getExtremes().min && s.xData[i] <= s.xAxis.getExtremes().max) {
                pairs.push([s.xData[i], s.yData[i]])
            }
        }

        return pairs;
    },

    performance: function (s) {
        return $.ajax({
            url: "{{ url_for('.', filename='performance') }}",
            type: "POST",
            data: JSON.stringify(performance.truncate(s)),
            contentType: "application/json; charset=utf-8"
        });
    },


    monthtable: function (s) {
        return $.ajax({
            url: "{{ url_for('.', filename='month') }}",
            type: "POST",
            data: JSON.stringify(s),
            contentType: "application/json; charset=utf-8"
        });
    },

    drawdown: function (s) {
        return $.ajax({
            url: "{{ url_for('.', filename='drawdown') }}",
            type: "POST",
            data: JSON.stringify(s),
            contentType: "application/json; charset=utf-8",
        });
    },

    volatility: function (s) {
        return $.ajax({
            url: "{{ url_for('.', filename='volatility') }}",
            type: "POST",
            data: JSON.stringify(s),
            contentType: "application/json; charset=utf-8",
        });
    }
};


const report = {
    initColumns: function (columns) {
        var cols = [];

        $.each(columns, function (i, val) {
            cols.push({"data": val, "render": function(data, type, row, meta) {return data;}, "defaultContent": "", "title": val});
        });

        return cols;
    },

    performanceTable: function (dom) {
        const header = ["name", "value"];

        return $(dom).dataTable({
            scrollX: false,
            paging: false,
            columns: report.initColumns(header),
            bFilter: false,
            info: false,
            bSort: false
        });
    },

    monthTable: function (dom) {
        const header = ["Year", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "STDev", "YTD"];

        return $(dom).dataTable({
            columns: report.initColumns(header),
            scrollX: false,
            bFilter: false,
            paging: false,
            info: false,
            bSort: false,
            order: [[0, "desc"]]
        })
    },
};
