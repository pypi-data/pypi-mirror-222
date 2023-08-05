/*! For license information please see 9343.68df0c5454cb71b71ac8.js.LICENSE.txt */
"use strict";(self.webpackChunkjupyterlab_nodeeditor=self.webpackChunkjupyterlab_nodeeditor||[]).push([[9343],{9343:(e,n,t)=>{t.r(n),t.d(n,{conf:()=>o,language:()=>r});var o={comments:{lineComment:"//",blockComment:["/*","*/"]},brackets:[["{","}"],["[","]"],["(",")"]],autoClosingPairs:[{open:"{",close:"}"},{open:"[",close:"]"},{open:"(",close:")"},{open:"'",close:"'",notIn:["string","comment"]},{open:'"',close:'"',notIn:["string"]},{open:"`",close:"`",notIn:["string","comment"]},{open:"/**",close:" */",notIn:["string"]}],surroundingPairs:[{open:"{",close:"}"},{open:"[",close:"]"},{open:"(",close:")"},{open:"<",close:">"},{open:"'",close:"'"},{open:"(",close:")"},{open:'"',close:'"'},{open:"`",close:"`"}],folding:{markers:{start:/^\s*\s*#?region\b/,end:/^\s*\s*#?endregion\b/}}},r={defaultToken:"invalid",tokenPostfix:".dart",keywords:["abstract","dynamic","implements","show","as","else","import","static","assert","enum","in","super","async","export","interface","switch","await","extends","is","sync","break","external","library","this","case","factory","mixin","throw","catch","false","new","true","class","final","null","try","const","finally","on","typedef","continue","for","operator","var","covariant","Function","part","void","default","get","rethrow","while","deferred","hide","return","with","do","if","set","yield"],typeKeywords:["int","double","String","bool"],operators:["+","-","*","/","~/","%","++","--","==","!=",">","<",">=","<=","=","-=","/=","%=",">>=","^=","+=","*=","~/=","<<=","&=","!=","||","&&","&","|","^","~","<<",">>","!",">>>","??","?",":","|="],symbols:/[=><!~?:&|+\-*\/\^%]+/,escapes:/\\(?:[abfnrtv\\"']|x[0-9A-Fa-f]{1,4}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})/,digits:/\d+(_+\d+)*/,octaldigits:/[0-7]+(_+[0-7]+)*/,binarydigits:/[0-1]+(_+[0-1]+)*/,hexdigits:/[[0-9a-fA-F]+(_+[0-9a-fA-F]+)*/,regexpctl:/[(){}\[\]\$\^|\-*+?\.]/,regexpesc:/\\(?:[bBdDfnrstvwWn0\\\/]|@regexpctl|c[A-Z]|x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4})/,tokenizer:{root:[[/[{}]/,"delimiter.bracket"],{include:"common"}],common:[[/[a-z_$][\w$]*/,{cases:{"@typeKeywords":"type.identifier","@keywords":"keyword","@default":"identifier"}}],[/[A-Z_$][\w\$]*/,"type.identifier"],{include:"@whitespace"},[/\/(?=([^\\\/]|\\.)+\/([gimsuy]*)(\s*)(\.|;|,|\)|\]|\}|$))/,{token:"regexp",bracket:"@open",next:"@regexp"}],[/@[a-zA-Z]+/,"annotation"],[/[()\[\]]/,"@brackets"],[/[<>](?!@symbols)/,"@brackets"],[/!(?=([^=]|$))/,"delimiter"],[/@symbols/,{cases:{"@operators":"delimiter","@default":""}}],[/(@digits)[eE]([\-+]?(@digits))?/,"number.float"],[/(@digits)\.(@digits)([eE][\-+]?(@digits))?/,"number.float"],[/0[xX](@hexdigits)n?/,"number.hex"],[/0[oO]?(@octaldigits)n?/,"number.octal"],[/0[bB](@binarydigits)n?/,"number.binary"],[/(@digits)n?/,"number"],[/[;,.]/,"delimiter"],[/"([^"\\]|\\.)*$/,"string.invalid"],[/'([^'\\]|\\.)*$/,"string.invalid"],[/"/,"string","@string_double"],[/'/,"string","@string_single"]],whitespace:[[/[ \t\r\n]+/,""],[/\/\*\*(?!\/)/,"comment.doc","@jsdoc"],[/\/\*/,"comment","@comment"],[/\/\/\/.*$/,"comment.doc"],[/\/\/.*$/,"comment"]],comment:[[/[^\/*]+/,"comment"],[/\*\//,"comment","@pop"],[/[\/*]/,"comment"]],jsdoc:[[/[^\/*]+/,"comment.doc"],[/\*\//,"comment.doc","@pop"],[/[\/*]/,"comment.doc"]],regexp:[[/(\{)(\d+(?:,\d*)?)(\})/,["regexp.escape.control","regexp.escape.control","regexp.escape.control"]],[/(\[)(\^?)(?=(?:[^\]\\\/]|\\.)+)/,["regexp.escape.control",{token:"regexp.escape.control",next:"@regexrange"}]],[/(\()(\?:|\?=|\?!)/,["regexp.escape.control","regexp.escape.control"]],[/[()]/,"regexp.escape.control"],[/@regexpctl/,"regexp.escape.control"],[/[^\\\/]/,"regexp"],[/@regexpesc/,"regexp.escape"],[/\\\./,"regexp.invalid"],[/(\/)([gimsuy]*)/,[{token:"regexp",bracket:"@close",next:"@pop"},"keyword.other"]]],regexrange:[[/-/,"regexp.escape.control"],[/\^/,"regexp.invalid"],[/@regexpesc/,"regexp.escape"],[/[^\]]/,"regexp"],[/\]/,{token:"regexp.escape.control",next:"@pop",bracket:"@close"}]],string_double:[[/[^\\"\$]+/,"string"],[/[^\\"]+/,"string"],[/@escapes/,"string.escape"],[/\\./,"string.escape.invalid"],[/"/,"string","@pop"],[/\$\w+/,"identifier"]],string_single:[[/[^\\'\$]+/,"string"],[/@escapes/,"string.escape"],[/\\./,"string.escape.invalid"],[/'/,"string","@pop"],[/\$\w+/,"identifier"]]}}}}]);