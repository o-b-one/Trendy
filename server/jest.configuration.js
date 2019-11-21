module.exports = {
    "clearMocks": true,

    "transform": {
        "^.+\\.(ts|tsx)?$": "ts-jest"
    },
    
    "globals":{
        "ts-jest": {
            "skipBabel": true,
            "enableTsDiagnostics": true
        }
    },
    "moduleFileExtensions": [
        "js",
        "ts",
        "json",
        "jsx",
        "node"
    ],
    
    "preset":"ts-jest",

    "testMatch": [
        "**/__tests__/**/?(*.)+(spec|test).(j|t)s?(x)",
        "**/__tests__/?(*.)+(spec|test).(j|t)s?(x)",
        "**/?(*.)+(spec|test).(j|t)s?(x)"
    ],

    "testPathIgnorePatterns": [
        "\\\\node_modules\\\\"
    ],

    "preset": "ts-jest",

    "testEnvironment": "node"
};