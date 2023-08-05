/* Copyright 2022 Karlsruhe Institute of Technology
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

/** Mixin to add common functionality to dashboard settings Vue components. */
export default {
  data() {
    return {
      settings_: {},
    };
  },
  props: {
    id: String,
    settings: Object,
    endpoints: Object,
  },
  watch: {
    id() {
      this.settings_ = kadi.utils.deepClone(this.settings);
    },
    settings_: {
      handler() {
        this.$emit('settings-updated', this.settings_);
      },
      deep: true,
    },
  },
};
