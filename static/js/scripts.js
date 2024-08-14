// Sentiment Chart
var ctx1 = document.getElementById('sentimentChart').getContext('2d');
var sentimentChart = new Chart(ctx1, {
    type: 'pie',
    data: {
        labels: ['Positive', 'Neutral', 'Negative'],
        datasets: [{
            data: [sentimentData.positiveCount, sentimentData.neutralCount, sentimentData.negativeCount],
            backgroundColor: ['#4CAF50', '#FFC107', '#F44336']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Trend Chart
var ctx2 = document.getElementById('trendChart').getContext('2d');
var trendChart = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
        datasets: [{
            label: 'Views',
            data: trendData,
            fill: false,
            borderColor: '#42A5F5',
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});
