(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[405],{5557:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return n(8377)}])},7498:function(e,t){"use strict";var n,r;Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var n in t)Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}(t,{PrefetchKind:function(){return n},ACTION_REFRESH:function(){return o},ACTION_NAVIGATE:function(){return i},ACTION_RESTORE:function(){return a},ACTION_SERVER_PATCH:function(){return c},ACTION_PREFETCH:function(){return l},ACTION_FAST_REFRESH:function(){return s},ACTION_SERVER_ACTION:function(){return d}});let o="refresh",i="navigate",a="restore",c="server-patch",l="prefetch",s="fast-refresh",d="server-action";(r=n||(n={})).AUTO="auto",r.FULL="full",r.TEMPORARY="temporary",("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},30:function(e,t,n){"use strict";function getDomainLocale(e,t,n,r){return!1}Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"getDomainLocale",{enumerable:!0,get:function(){return getDomainLocale}}),n(2866),("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},5170:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return v}});let r=n(8754),o=r._(n(7294)),i=n(4450),a=n(2227),c=n(4364),l=n(109),s=n(3607),d=n(1823),u=n(9031),f=n(920),p=n(30),h=n(7192),g=n(7498),b=new Set;function prefetch(e,t,n,r,o,i){if(!i&&!(0,a.isLocalURL)(t))return;if(!r.bypassPrefetchedCheck){let o=void 0!==r.locale?r.locale:"locale"in e?e.locale:void 0,i=t+"%"+n+"%"+o;if(b.has(i))return;b.add(i)}let c=i?e.prefetch(t,o):e.prefetch(t,n,r);Promise.resolve(c).catch(e=>{})}function isModifiedEvent(e){let t=e.currentTarget,n=t.getAttribute("target");return n&&"_self"!==n||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.nativeEvent&&2===e.nativeEvent.which}function linkClicked(e,t,n,r,i,c,l,s,d,u){let{nodeName:f}=e.currentTarget,p="A"===f.toUpperCase();if(p&&(isModifiedEvent(e)||!d&&!(0,a.isLocalURL)(n)))return;e.preventDefault();let navigate=()=>{let e=null==l||l;"beforePopState"in t?t[i?"replace":"push"](n,r,{shallow:c,locale:s,scroll:e}):t[i?"replace":"push"](r||n,{forceOptimisticNavigation:!u,scroll:e})};d?o.default.startTransition(navigate):navigate()}function formatStringOrUrl(e){return"string"==typeof e?e:(0,c.formatUrl)(e)}let m=o.default.forwardRef(function(e,t){let n,r;let{href:a,as:c,children:b,prefetch:m=null,passHref:v,replace:k,shallow:y,scroll:_,locale:C,onClick:w,onMouseEnter:x,onTouchStart:E,legacyBehavior:O=!1,...j}=e;n=b,O&&("string"==typeof n||"number"==typeof n)&&(n=o.default.createElement("a",null,n));let L=o.default.useContext(d.RouterContext),Z=o.default.useContext(u.AppRouterContext),S=null!=L?L:Z,N=!L,M=!1!==m,A=null===m?g.PrefetchKind.AUTO:g.PrefetchKind.FULL,{href:P,as:I}=o.default.useMemo(()=>{if(!L){let e=formatStringOrUrl(a);return{href:e,as:c?formatStringOrUrl(c):e}}let[e,t]=(0,i.resolveHref)(L,a,!0);return{href:e,as:c?(0,i.resolveHref)(L,c):t||e}},[L,a,c]),T=o.default.useRef(P),R=o.default.useRef(I);O&&(r=o.default.Children.only(n));let z=O?r&&"object"==typeof r&&r.ref:t,[X,B,U]=(0,f.useIntersection)({rootMargin:"200px"}),D=o.default.useCallback(e=>{(R.current!==I||T.current!==P)&&(U(),R.current=I,T.current=P),X(e),z&&("function"==typeof z?z(e):"object"==typeof z&&(z.current=e))},[I,z,P,U,X]);o.default.useEffect(()=>{S&&B&&M&&prefetch(S,P,I,{locale:C},{kind:A},N)},[I,P,B,C,M,null==L?void 0:L.locale,S,N,A]);let H={ref:D,onClick(e){O||"function"!=typeof w||w(e),O&&r.props&&"function"==typeof r.props.onClick&&r.props.onClick(e),S&&!e.defaultPrevented&&linkClicked(e,S,P,I,k,y,_,C,N,M)},onMouseEnter(e){O||"function"!=typeof x||x(e),O&&r.props&&"function"==typeof r.props.onMouseEnter&&r.props.onMouseEnter(e),S&&(M||!N)&&prefetch(S,P,I,{locale:C,priority:!0,bypassPrefetchedCheck:!0},{kind:A},N)},onTouchStart(e){O||"function"!=typeof E||E(e),O&&r.props&&"function"==typeof r.props.onTouchStart&&r.props.onTouchStart(e),S&&(M||!N)&&prefetch(S,P,I,{locale:C,priority:!0,bypassPrefetchedCheck:!0},{kind:A},N)}};if((0,l.isAbsoluteUrl)(I))H.href=I;else if(!O||v||"a"===r.type&&!("href"in r.props)){let e=void 0!==C?C:null==L?void 0:L.locale,t=(null==L?void 0:L.isLocaleDomain)&&(0,p.getDomainLocale)(I,e,null==L?void 0:L.locales,null==L?void 0:L.domainLocales);H.href=t||(0,h.addBasePath)((0,s.addLocale)(I,e,null==L?void 0:L.defaultLocale))}return O?o.default.cloneElement(r,H):o.default.createElement("a",{...j,...H},n)}),v=m;("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},920:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"useIntersection",{enumerable:!0,get:function(){return useIntersection}});let r=n(7294),o=n(3436),i="function"==typeof IntersectionObserver,a=new Map,c=[];function createObserver(e){let t;let n={root:e.root||null,margin:e.rootMargin||""},r=c.find(e=>e.root===n.root&&e.margin===n.margin);if(r&&(t=a.get(r)))return t;let o=new Map,i=new IntersectionObserver(e=>{e.forEach(e=>{let t=o.get(e.target),n=e.isIntersecting||e.intersectionRatio>0;t&&n&&t(n)})},e);return t={id:n,observer:i,elements:o},c.push(n),a.set(n,t),t}function observe(e,t,n){let{id:r,observer:o,elements:i}=createObserver(n);return i.set(e,t),o.observe(e),function(){if(i.delete(e),o.unobserve(e),0===i.size){o.disconnect(),a.delete(r);let e=c.findIndex(e=>e.root===r.root&&e.margin===r.margin);e>-1&&c.splice(e,1)}}}function useIntersection(e){let{rootRef:t,rootMargin:n,disabled:a}=e,c=a||!i,[l,s]=(0,r.useState)(!1),d=(0,r.useRef)(null),u=(0,r.useCallback)(e=>{d.current=e},[]);(0,r.useEffect)(()=>{if(i){if(c||l)return;let e=d.current;if(e&&e.tagName){let r=observe(e,e=>e&&s(e),{root:null==t?void 0:t.current,rootMargin:n});return r}}else if(!l){let e=(0,o.requestIdleCallback)(()=>s(!0));return()=>(0,o.cancelIdleCallback)(e)}},[c,n,t,l,d.current]);let f=(0,r.useCallback)(()=>{s(!1)},[]);return[u,l,f]}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},8377:function(e,t,n){"use strict";n.r(t),n.d(t,{Link_2505450bd85c8571cd6b01ace5708f5d:function(){return Link_2505450bd85c8571cd6b01ace5708f5d},Link_eb856c3168284879c63f34b3f73da8bb:function(){return Link_eb856c3168284879c63f34b3f73da8bb},default:function(){return Component}});var r=n(2364),o=n(7294),i=n(8531),a=n(6608),c=n(1664),l=n.n(c),s={xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:2,strokeLinecap:"round",strokeLinejoin:"round"};/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let toKebabCase=e=>e.replace(/([a-z0-9])([A-Z])/g,"$1-$2").toLowerCase(),createLucideIcon=(e,t)=>{let n=(0,o.forwardRef)(({color:n="currentColor",size:r=24,strokeWidth:i=2,absoluteStrokeWidth:a,className:c="",children:l,...d},u)=>(0,o.createElement)("svg",{ref:u,...s,width:r,height:r,stroke:n,strokeWidth:a?24*Number(i)/Number(r):i,className:["lucide",`lucide-${toKebabCase(e)}`,c].join(" "),...d},[...t.map(([e,t])=>(0,o.createElement)(e,t)),...Array.isArray(l)?l:[l]]));return n.displayName=`${e}`,n},d=createLucideIcon("Github",[["path",{d:"M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4",key:"tonef"}],["path",{d:"M9 18c-4.51 2-5-2-7-2",key:"9comsn"}]]),u=createLucideIcon("Linkedin",[["path",{d:"M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z",key:"c2jq9f"}],["rect",{width:"4",height:"12",x:"2",y:"9",key:"mk3on5"}],["circle",{cx:"4",cy:"4",r:"2",key:"bt5ra8"}]]);var f=n(9008),p=n.n(f);function Link_eb856c3168284879c63f34b3f73da8bb(){return(0,r.tZ)(i.rU,{asChild:!0,css:{width:"100%","&:hover":{color:"var(--accent-8)"}},target:(0,a.oA)(!0)?"_blank":"",children:(0,r.tZ)(l(),{href:"https://github.com/NoMeLlamoDante",passHref:!0,children:(0,r.tZ)(i.zx,{css:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"0.5em",background:"#3b3338",color:"#fff9e4","&:hover":{background:"#004638",color:"#fff9e4"}},children:(0,r.BX)(i.kC,{align:"center",className:"rx-Stack",css:{widht:"100%",alt:"Github"},direction:"row",gap:"3",children:[(0,r.tZ)(d,{css:{color:"var(--current-color)"}}),(0,r.tZ)(i.xv,{as:"p",css:{"font-size":"1.5em","font-weight":"bold"},children:"Github"})]})})})})}function Link_2505450bd85c8571cd6b01ace5708f5d(){return(0,r.tZ)(i.rU,{asChild:!0,css:{width:"100%","&:hover":{color:"var(--accent-8)"}},target:(0,a.oA)(!0)?"_blank":"",children:(0,r.tZ)(l(),{href:"https://www.linkedin.com/in/edgar-zarate-61285bba/",passHref:!0,children:(0,r.tZ)(i.zx,{css:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"0.5em",background:"#3b3338",color:"#fff9e4","&:hover":{background:"#004638",color:"#fff9e4"}},children:(0,r.BX)(i.kC,{align:"center",className:"rx-Stack",css:{widht:"100%",alt:"linkedin"},direction:"row",gap:"3",children:[(0,r.tZ)(u,{css:{color:"var(--current-color)"}}),(0,r.tZ)(i.xv,{as:"p",css:{"font-size":"1.5em","font-weight":"bold"},children:"linkedin"})]})})})})}function Component(){return(0,r.BX)(o.Fragment,{children:[(0,r.tZ)(i.kC,{children:(0,r.BX)(i.xu,{css:{width:"100%",justify:"center",align:"center"},children:[(0,r.BX)(i.kC,{align:"start",className:"rx-Stack",css:{alignItems:"center",position:"sticky",paddingInlineStart:"2em",paddingInlineEnd:"2em",paddingTop:"0.5em",paddingBottom:"0.5em",top:"0px",width:"100%",background:"#004638"},direction:"row",justify:"between",gap:"3",children:[(0,r.tZ)(i.X6,{size:"7",weight:"bold",children:"Edgar Zarate"}),(0,r.tZ)(i.X6,{size:"3",weight:"medium",children:"Dante"})]}),(0,r.tZ)(i.kC,{css:{display:"flex",alignItems:"center",justifyContent:"center",paddingTop:"1.5em",paddingBottom:"1.5em"},children:(0,r.BX)(i.kC,{align:"center",className:"rx-Stack",css:{maxWidth:"80%"},direction:"column",justify:"center",gap:"3",children:[(0,r.BX)(i.kC,{align:"center",className:"rx-Stack",direction:"column",justify:"center",gap:"5",children:[(0,r.BX)(i.kC,{align:"center",className:"rx-Stack",direction:"row",justify:"center",gap:"3",children:[(0,r.tZ)(i.qE,{css:{zIndex:"-1",alt:"Logotipo de Edgar Zarate"},fallback:"Dante",highContrast:!1,radius:"large",size:"7",src:"SB3Ail01.svg",variant:"solid"}),(0,r.BX)(i.kC,{align:"center",className:"rx-Stack",direction:"column",justify:"start",gap:"1",children:[(0,r.tZ)(i.X6,{css:{fontSize:"2em",justifyContent:"center",textAlign:"center",width:"100%",color:"#6dedb2"},children:"Edgar Zarate"}),(0,r.tZ)(i.xv,{as:"p",size:"2",children:"Desarrollador web y mas"})]})]}),(0,r.tZ)(i.xv,{as:"p",css:{fontSize:"0.8em",maxWidth:"60%"},children:"Hola, Mi nombre es Edgar  pero mis amigos me llaman Dante, \n            soy un desarrollador de software, me gusta la programaci\xf3n y la tecnolog\xeda\n            en general."})]}),(0,r.tZ)(i.Z0,{size:"4"}),(0,r.BX)(i.kC,{align:"start",className:"rx-Stack",direction:"column",gap:"3",children:[(0,r.tZ)(i.X6,{css:{fontSize:"2em",justifyContent:"center",textAlign:"center",width:"100%",color:"#6dedb2"},children:"Links"}),(0,r.tZ)(Link_eb856c3168284879c63f34b3f73da8bb,{}),(0,r.tZ)(Link_2505450bd85c8571cd6b01ace5708f5d,{})]})]})}),(0,r.BX)(i.kC,{align:"center",className:"rx-Stack",css:{width:"100%"},direction:"column",gap:"3",children:[(0,r.tZ)("img",{css:{width:"50px"},src:"favicon.ico"}),(0,r.tZ)(i.xv,{as:"p",css:{fontSize:"0.8em"},children:"learning to dream in code"}),(0,r.tZ)(i.xv,{as:"p",css:{fontSize:"0.8em"},children:"2023-2024"})]})]})}),(0,r.BX)(p(),{children:[(0,r.tZ)("title",{children:"Edgar | Dante Desarrollador de Software"}),(0,r.tZ)("meta",{content:"P\xe1gina de perfil de Edgar Zarate, desarrollador de software.",name:"description"}),(0,r.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}},9008:function(e,t,n){e.exports=n(9201)},1664:function(e,t,n){e.exports=n(5170)}},function(e){e.O(0,[774,888,179],function(){return e(e.s=5557)}),_N_E=e.O()}]);