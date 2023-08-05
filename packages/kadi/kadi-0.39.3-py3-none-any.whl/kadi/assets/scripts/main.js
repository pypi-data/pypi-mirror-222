/* Copyright 2020 Karlsruhe Institute of Technology
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License. */

import axios from 'axios';
import dayjs from 'dayjs';
import i18next from 'i18next';
import jQuery from 'jquery';
import Vue from 'vue';
import 'bootstrap';
import 'select2/dist/js/select2.full.js';

// Additional imports for Day.js
import LocalizedFormat from 'dayjs/plugin/localizedFormat';
import RelativeTime from 'dayjs/plugin/relativeTime';
import 'dayjs/locale/de';

import translations from 'translations/translations';
import utils from 'scripts/lib/utils';
import 'styles/main.scss';

// Namespace for globally accessible objects.
window.kadi = kadi;
// Namespace for global utility functions.
window.kadi.utils = utils;

window.$t = i18next.t;
window.$ = window.jQuery = jQuery;
window.axios = axios;
window.dayjs = dayjs;
window.i18next = i18next;
window.Vue = Vue;

// Global axios settings.
axios.defaults.headers.common['X-CSRF-TOKEN'] = kadi.globals.csrf_token;
axios.defaults.params = {_internal: true};
axios.defaults.paramsSerializer = {indexes: null};

// Global Day.js settings.
dayjs.locale(kadi.globals.locale);
dayjs.extend(LocalizedFormat);
dayjs.extend(RelativeTime);

// Global i18next settings.
i18next.init({
  // Until i18next-scanner supports the newer format.
  compatibilityJSON: 'v3',
  fallbackLng: false,
  keySeparator: false,
  lng: kadi.globals.locale,
  nsSeparator: false,
  resources: translations,
  returnEmptyString: false,
  supportedLngs: Object.keys(translations),
});

// Global jQuery settings.
$.ajaxSetup({
  headers: {'X-CSRF-TOKEN': kadi.globals.csrf_token},
  traditional: true,
});

// Global Vue settings.
Vue.options.delimiters = ['{$', '$}']; // For using Vue and Jinja in the same template.

Vue.prototype.kadi = kadi;
Vue.prototype.$t = i18next.t;
Vue.prototype.$ = Vue.prototype.jQuery = jQuery;

// Global Vue filters.
Vue.filter('capitalize', kadi.utils.capitalize);
Vue.filter('filesize', kadi.utils.filesize);
Vue.filter('prettyTypeName', kadi.utils.prettyTypeName);
Vue.filter('truncate', kadi.utils.truncate);

// Global Vue components. All components inside 'components/global' are registered.
const requireComponent = require.context('./components/global', true, /\.vue$/);

requireComponent.keys().forEach((fileName) => {
  const componentConfig = requireComponent(fileName);
  const componentName = fileName.split('/').pop().replace(/\.\w+$/, '');
  Vue.component(componentName, componentConfig.default);
});

// Global Bootstrap settings.
const whiteList = $.fn.popover.Constructor.Default.whiteList;
whiteList.button = [];
whiteList.dd = [];
whiteList.dl = [];
whiteList.dt = [];
whiteList.table = [];
whiteList.tbody = [];
whiteList.td = [];
whiteList.th = [];
whiteList.thead = [];
whiteList.tr = [];

// Global Select2 settings.
$.fn.select2.defaults.set('theme', 'bootstrap4');
