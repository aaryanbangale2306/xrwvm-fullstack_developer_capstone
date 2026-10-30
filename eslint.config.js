import js from "@eslint/js";

export default [
    js.configs.recommended,
    {
        files: ["server/frontend/src/**/*.js", "server/frontend/src/**/*.jsx"],
        languageOptions: {
            ecmaVersion: 2022,
            sourceType: "module",
            parserOptions: {
                ecmaFeatures: {
                    jsx: true
                }
            },
            globals: {
                console: "readonly",
                window: "readonly",
                document: "readonly",
                sessionStorage: "readonly",
                alert: "readonly",
                fetch: "readonly"
            }
        },
        rules: {
            "no-unused-vars": "off"
        }
    }
];