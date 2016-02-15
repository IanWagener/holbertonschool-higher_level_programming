var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
        'User-Agent': 'Holberton_School',
        'Authorization': 'token ' + process.env.TOKEN
    }
};

var req = https.request(options, function(res) {
    var fs = require('fs');
    fs.writeFile("/tmp/15", ,function(err) {
        if(err) {
            return console.log(err);
        }

        console.log("The file was saved!");
    });
});
req.end();

req.on('error', function(e) {
    console.error(e);
});

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
        chunks.push(chunk);
    });
    stream.on('end', () => {
        cb(chunks.join(''));
    });
}