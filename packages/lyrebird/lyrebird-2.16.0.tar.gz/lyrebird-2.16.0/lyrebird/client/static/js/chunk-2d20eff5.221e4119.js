(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d20eff5"],{b26e:function(e,n,o){"use strict";o.r(n),o.d(n,"conf",function(){return t}),o.d(n,"language",function(){return s});var t={comments:{blockComment:["/*","*/"],lineComment:"//"},brackets:[["{","}"],["[","]"],["(",")"]],autoClosingPairs:[{open:"{",close:"}",notIn:["string"]},{open:"[",close:"]",notIn:["string"]},{open:"(",close:")",notIn:["string"]},{open:'"',close:'"',notIn:["string"]},{open:"'",close:"'",notIn:["string"]}],surroundingPairs:[{open:"{",close:"}"},{open:"[",close:"]"},{open:"(",close:")"},{open:'"',close:'"'},{open:"'",close:"'"},{open:"<",close:">"}]},s={defaultToken:"",tokenPostfix:".flow",keywords:["import","require","export","forbid","native","if","else","cast","unsafe","switch","default"],types:["io","mutable","bool","int","double","string","flow","void","ref","true","false","with"],operators:["=",">","<","<=",">=","==","!","!=",":=","::=","&&","||","+","-","*","/","@","&","%",":","->","\\","$","??","^"],symbols:/[@$=><!~?:&|+\-*\\\/\^%]+/,escapes:/\\(?:[abfnrtv\\"']|x[0-9A-Fa-f]{1,4}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})/,tokenizer:{root:[[/[a-zA-Z_]\w*/,{cases:{"@keywords":"keyword","@types":"type","@default":"identifier"}}],{include:"@whitespace"},[/[{}()\[\]]/,"delimiter"],[/[<>](?!@symbols)/,"delimiter"],[/@symbols/,{cases:{"@operators":"delimiter","@default":""}}],[/((0(x|X)[0-9a-fA-F]*)|(([0-9]+\.?[0-9]*)|(\.[0-9]+))((e|E)(\+|-)?[0-9]+)?)/,"number"],[/[;,.]/,"delimiter"],[/"([^"\\]|\\.)*$/,"string.invalid"],[/"/,"string","@string"]],whitespace:[[/[ \t\r\n]+/,""],[/\/\*/,"comment","@comment"],[/\/\/.*$/,"comment"]],comment:[[/[^\/*]+/,"comment"],[/\*\//,"comment","@pop"],[/[\/*]/,"comment"]],string:[[/[^\\"]+/,"string"],[/@escapes/,"string.escape"],[/\\./,"string.escape.invalid"],[/"/,"string","@pop"]]}}}}]);