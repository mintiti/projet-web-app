webpackJsonp([1],{"+zE0":function(t,o){},NHnr:function(t,o,a){"use strict";Object.defineProperty(o,"__esModule",{value:!0});var e=a("7+uW"),s={render:function(){this.$createElement;this._self._c;return this._m(0)},staticRenderFns:[function(){var t=this,o=t.$createElement,a=t._self._c||o;return a("div",{staticClass:"left-nav"},[a("ul",[a("li",[a("i",{staticClass:"icon iconfont icon-goumai"}),t._v(" "),a("div",[t._v("cashier")])]),t._v(" "),a("li",[a("i",{staticClass:"icon iconfont icon-dianpu"}),t._v(" "),a("div",[t._v("shop")])]),t._v(" "),a("li",[a("i",{staticClass:"icon iconfont icon-hanbao"}),t._v(" "),a("div",[t._v("product")])]),t._v(" "),a("li",[a("i",{staticClass:"icon iconfont icon-huiyuanqia"}),t._v(" "),a("div",[t._v("member")])]),t._v(" "),a("li",[a("i",{staticClass:"icon iconfont icon-goumai"}),t._v(" "),a("div",[t._v("addtion")])]),t._v(" "),a("li",[a("i",{staticClass:"icon iconfont icon-gongnengjianyi"}),t._v(" "),a("div",[t._v("setting")])])])])}]};var n={name:"App",components:{leftNav:a("VU/8")({},s,!1,function(t){a("ewDi")},null,null).exports}},i={render:function(){var t=this.$createElement,o=this._self._c||t;return o("div",{attrs:{id:"app"}},[o("leftNav"),this._v(" "),o("div"),this._v(" "),o("router-view")],1)},staticRenderFns:[]};var l=a("VU/8")(n,i,!1,function(t){a("+zE0")},null,null).exports,c=a("/ocq"),r=a("mtWM"),d=a.n(r),u={name:"shop",data:function(){return{tableData:[],oftenGoods:[],type0Goods:[],type1Goods:[],type2Goods:[],type3Goods:[],totalMoney:0,totlaCount:0}},created:function(){var t=this;d.a.get("https://www.fastmock.site/mock/0bf6a5bae7eab8507e44b56191ddff36/vuepos/oftenGoods").then(function(o){t.oftenGoods=o.data.oftenGoods}).catch(function(t){alert("Internet Error")}),d.a.get("https://www.fastmock.site/mock/0bf6a5bae7eab8507e44b56191ddff36/vuepos/typeGoods").then(function(o){t.type0Goods=o.data.data[0],t.type1Goods=o.data.data[1],t.type2Goods=o.data.data[2],t.type3Goods=o.data.data[3]}).catch(function(t){alert("Internet Error")})},mounted:function(){var t=document.body.clientHeight;document.getElementById("order-list").style.height=t+"px"},methods:{addOrderList:function(t){var o=this;this.totalCount=0,this.totalMoney=0;for(var a=!1,e=0;e<this.tableData.length;e++)this.tableData[e].goodsId==t.goodsId&&(a=!0);if(a){this.tableData.filter(function(o){return o.goodsId==t.goodsId})[0].count++}else{var s={goodsId:t.goodsId,goodsName:t.goodsName,price:t.price,count:1};this.tableData.push(s),this.tableData.forEach(function(t){o.totalCount+=t.count,o.totalMoney=o.totalMoney+t.price*t.count})}},delSingleGoods:function(t){this.tableData=this.tableData.filter(function(o){return o.goodsId!=t.goodsId})},delAllGoods:function(){this.tableData=[],this.totalCount=0,this.totalMoney=0},checkout:function(){0!=this.totalCount?(this.tableData=[],this.totlaCount=0,this.totalMoney=0,this.$message({message:"Thank You!",type:"success"})):this.$message.error("Please add items before checkout!")}}},v={render:function(){var t=this,o=t.$createElement,a=t._self._c||o;return a("div",{staticClass:"shop"},[a("el-row",[a("el-col",{staticClass:"pos-order",attrs:{span:7,id:"order-list"}},[a("el-tabs",[a("el-tab-pane",{attrs:{label:"Order"}},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.tableData,border:""}},[a("el-table-column",{attrs:{prop:"goodsName",label:"Goodsname"}}),t._v(" "),a("el-table-column",{attrs:{prop:"count",label:"Count"}}),t._v(" "),a("el-table-column",{attrs:{prop:"price",label:"Price"}}),t._v(" "),a("el-table-column",{attrs:{prop:"do",label:"Do",fixed:"right"},scopedSlots:t._u([{key:"default",fn:function(o){return[a("el-button",{attrs:{type:"text",size:"small"},on:{click:function(a){return t.delSingleGoods(o.row)}}},[t._v("delete")]),t._v(" "),a("el-button",{attrs:{type:"text",size:"small"},on:{click:function(a){return t.addOrderList(o.row)}}},[t._v("add")])]}}])})],1),t._v(" "),a("div",{staticClass:"totaldiv"},[t._v("Number:"+t._s(t.totalCount)+"       Total price："+t._s(t.totalMoney))]),t._v(" "),a("div",{staticClass:"div-button"},[a("el-button",{attrs:{type:"danger"},on:{click:t.delAllGoods}},[t._v("CANCAL")]),t._v(" "),a("el-button",{attrs:{type:"success"},on:{click:t.checkout}},[t._v("BUY")])],1)],1),t._v(" "),a("el-tab-pane",{attrs:{label:"Buy"}},[t._v("Buy")]),t._v(" "),a("el-tab-pane",{attrs:{label:"Takeaway"}},[t._v("Takeaway")])],1)],1),t._v(" "),a("el-col",{attrs:{span:17}},[a("div",{staticClass:"often-goods"},[a("div",{staticClass:"title"},[t._v("favorite goods")]),t._v(" "),a("div",{staticClass:"often-goods-list"},[a("ul",t._l(t.oftenGoods,function(o){return a("li",{on:{click:function(a){return t.addOrderList(o)}}},[a("span",[t._v(t._s(o.goodsName))]),t._v(" "),a("span",{staticClass:"o-price"},[t._v(t._s(o.price)+"EUR")])])}),0)])]),t._v(" "),a("div",{staticClass:"goods-type"},[a("el-tabs",[a("el-tab-pane",{attrs:{label:"buger"}},[a("div",[a("ul",{staticClass:"cookList"},t._l(t.type0Goods,function(o){return a("li",{on:{click:function(a){return t.addOrderList(o)}}},[a("span",{staticClass:"foodImg"},[a("img",{attrs:{src:o.goodsImg,width:"100%"}})]),t._v(" "),a("span",{staticClass:"foodName"},[t._v(t._s(o.goodsName))]),t._v(" "),a("span",{staticClass:"foodPrice"},[t._v(t._s(o.price)+"EUR")])])}),0)])]),t._v(" "),a("el-tab-pane",{attrs:{label:"snack"}},[t._v("\n            snack\n            "),a("ul",{staticClass:"cookList"},t._l(t.type1Goods,function(o){return a("li",{on:{click:function(a){return t.addOrderList(o)}}},[a("span",{staticClass:"foodImg"},[a("img",{attrs:{src:o.goodsImg,width:"100%"}})]),t._v(" "),a("span",{staticClass:"foodName"},[t._v(t._s(o.goodsName))]),t._v(" "),a("span",{staticClass:"foodPrice"},[t._v(t._s(o.price)+"EUR")])])}),0)]),t._v(" "),a("el-tab-pane",{attrs:{label:"drink"}},[t._v("\n            drink\n            "),a("ul",{staticClass:"cookList"},t._l(t.type2Goods,function(o){return a("li",{on:{click:function(a){return t.addOrderList(o)}}},[a("span",{staticClass:"foodImg"},[a("img",{attrs:{src:o.goodsImg,width:"100%"}})]),t._v(" "),a("span",{staticClass:"foodName"},[t._v(t._s(o.goodsName))]),t._v(" "),a("span",{staticClass:"foodPrice"},[t._v(t._s(o.price)+"EUR")])])}),0)]),t._v(" "),a("el-tab-pane",{attrs:{label:"menu"}},[t._v("\n            menu\n            "),a("ul",{staticClass:"cookList"},t._l(t.type3Goods,function(o){return a("li",{on:{click:function(a){return t.addOrderList(o)}}},[a("span",{staticClass:"foodImg"},[a("img",{attrs:{src:o.goodsImg,width:"100%"}})]),t._v(" "),a("span",{staticClass:"foodName"},[t._v(t._s(o.goodsName))]),t._v(" "),a("span",{staticClass:"foodPrice"},[t._v(t._s(o.price)+"EUR")])])}),0)])],1)],1)])],1)],1)},staticRenderFns:[]};var p=a("VU/8")(u,v,!1,function(t){a("rX6q")},"data-v-6ba8e950",null).exports;e.default.use(c.a);var f=new c.a({routes:[{path:"/",name:"shop",component:p}]}),_=a("zL8q"),m=a.n(_),h=(a("tvR6"),a("wUZ8")),b=a.n(h);e.default.use(m.a,{locale:b.a}),e.default.config.productionTip=!1,new e.default({el:"#app",router:f,template:"<App/>",components:{App:l}})},ewDi:function(t,o){},rX6q:function(t,o){},tvR6:function(t,o){}},["NHnr"]);
//# sourceMappingURL=app.6bc0610ea942e54ed65a.js.map