// Step 1: Set up our chart
//= ================================

var margin = {top: 20, right: 10, bottom: 30, left: 10},
    width = 2000 - margin.left - margin.right,
    height = 800 - margin.top - margin.bottom;

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("country_medal_data_test.csv").then(function(data) {
    var subgroups = data.columns.slice(0)

    var NOC = d3.map(data, function(d) {return(d.NOC)}).keys()

    var x = d3.scaleBand()
      .domain(NOC)
      .range([0, width])
      .padding([.0001])
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x).tickSizeOuter(0)); 

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([0, 6000])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisRight(y));
    
    // color palette = one color per subgroup
    var color = d3.scaleOrdinal()
      .domain(subgroups)
      .range(["#ffd700", "#c0c0c0","cd7f32"])

    //stack the data? --> stack per subgroup
    var stackedData = d3.stack()
        .keys(subgroups)
        (data)

    // Create a tooltip
  // ----------------
    var tooltip = d3.select("body")
      .append("div")
      .style("opacity", 0)
      .attr("class", "tooltip")
      .style("background-color", "white")
      .style("border", "solid")
      .style("border-width", "1px")
      .style("border-radius", "1px")
      .style("padding", "1px")

// Three function that change the tooltip when user hover / move / leave a cell
    var mouseover = function(d) {
        var subgroupName = d3.select(this.parentNode).datum().key;
        var subgroupValue = d.data[subgroupName];
        tooltip
            .html("Medal Type: " + subgroupName + "<br>" + "Total Medals: " + subgroupValue)
            .style("opacity", 1)
    }
    var mousemove = function(d) {
        tooltip
            .style("left", (d3.mouse(this)[0]+120) + "px") // It is important to put the +90: other wise the tooltip is exactly where the point is an it creates a weird effect
            .style("top", (d3.mouse(this)[1]) + "px")
    }
    var mouseleave = function(d) {
        tooltip
            .style("opacity", 0)
    }
    // Show the bars
    svg.append("g")
        .selectAll("g")
  // Enter in the stack data = loop key per key = group per group
        .data(stackedData)
        .enter().append("g")
        .attr("fill", function(d) { return color(d.key); })
        .selectAll("rect")
    // enter a second time = loop subgroup per subgroup to add all rectangles
        .data(function(d) { return d; })
        .enter().append("rect")
            .attr("x", function(d) { return x(d.data.NOC); })
            .attr("y", function(d) { return y(d[1]); })
            .attr("height", function(d) { return y(d[0]) - y(d[1]); })
            .attr("width",x.bandwidth())
            .attr("stroke", "grey")
        .on("mouseover", mouseover)
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave)

});
   