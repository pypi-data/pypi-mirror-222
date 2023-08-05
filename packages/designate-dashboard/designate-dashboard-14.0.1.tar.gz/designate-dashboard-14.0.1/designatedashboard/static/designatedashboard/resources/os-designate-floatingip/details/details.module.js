/**
 * (c) Copyright 2016 Hewlett Packard Enterprise Development LP
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

(function() {
  'use strict';

  /**
   * @ngdoc overview
   * @ngname designatedashboard.resources.os-designate-floatingip.details
   *
   * @description
   * Provides details features for floating IPs.
   */
  angular.module('designatedashboard.resources.os-designate-floatingip.details',
    ['horizon.framework.conf', 'horizon.app.core'])
    .run(run);

  run.$inject = [
    'designatedashboard.resources.os-designate-floatingip.resourceType',
    'designatedashboard.resources.os-designate-floatingip.api',
    'designatedashboard.resources.os-designate-floatingip.basePath',
    'horizon.framework.conf.resource-type-registry.service'
  ];

  function run(
    resourceTypeName,
    api,
    basePath,
    registry
  ) {
    var resourceType = registry.getResourceType(resourceTypeName);
    resourceType
      .setLoadFunction(loadFunction)
      .setSummaryTemplateUrl(basePath + 'details/drawer.html')
      .setItemNameFunction(itemNameFunction);

    resourceType.detailsViews
      .prepend({
        id: 'floatingIpDetailsOverview',
        name: gettext('Overview'),
        template: basePath + 'details/overview.html'
      }, 0);

    function loadFunction(identifier) {
      return api.get(identifier);
    }

    function itemNameFunction(floatingIp) {
      return floatingIp.address;
    }
  }

})();
