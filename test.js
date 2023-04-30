//q: how to do a basic hello world test?
//a: use the assert module


// a basic hello world test
var assert = require('assert');
describe('Basic Mocha String Test', function () {
    it('should return number of charachters in a string', function () {
        assert.equal("Hello".length, 4);
    });
    it('should return first charachter of the string', function () {
        assert.equal("Hello".charAt(0), 'H');
    });
}
);

// q: how to run the test?
// a: use the mocha command
