$(function(){

    this.makeGauge = function(selector, value, color)
    {
	c3.generate({
	    bindto: selector,
	    data: {
		columns: [
		    ['data', value]
		],
		type: 'gauge'
	    },
	    tooltip: {
		show: false
	    },
	    gauge: {
		label: {
		    format: function(value, ratio) {
			return value + '%';
		    },
		    show: false
		},
		min: 0,
		max: 100,
		units: ' %',
		width: 50
	    },
	    color: {
		pattern: [color, color, color], // the 3 color levels for the percentage values.
	    }
	});
    };

    this.makeGauge('#d1-c1', 42, '#1abc9c');
    this.makeGauge('#d1-c2', 22, '#3498db');
    this.makeGauge('#d1-c3', 72, '#f39c12');

    this.makeChart = function(selector, type, colors, legend)
    {
	c3.generate({
	    bindto: selector,
	    data: {
		x: 'x',
		//        xFormat: '%Y%m%d', // 'xFormat' can be used as custom format of 'x'
		columns: [
		    ['x', '2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06',
		     '2018-01-07', '2018-01-08', '2018-01-09', '2018-01-10', '2018-01-11', '2018-01-12'],
		    ['陌生人', 130, 340, 200, 500, 250, 350, 130, 333, 200, 500, 220, 350],
		    ['注册用户', 30, 200, 100, 400, 150, 250, 30, 200, 112, 322, 70, 300]
		],
		//type: 'spline'
		type: type
	    },
	    axis: {
		x: {
		    type: 'timeseries',
		    tick: {
			format: '%Y-%m-%d'
		    }
		},

		y: {
		    max: 500,
		    tick: {
			values: [100, 200, 300, 400, 500]
		    }
		}

	    },

	    legend: {
		show: legend,
		position: 'inset'
	    },

	    color: {
		pattern: colors
	    }

	});
    }

    //this.makeChart('#d1-c4', 'area-spline', ['#3498db', '#f39c12'], true);
    this.makeChart('#d1-c4', 'spline', ['#1abc9c', '#3498db'], true);
    //this.makeChart('#d1-c5', 'bar', ['#1abc9c', '#16a085', '#f39c12'], false);
    this.makeChart('#d1-c5', 'bar', ['#3498db', '#2980b9'], false);

});
