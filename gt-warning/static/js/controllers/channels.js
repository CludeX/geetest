angular.module('gtWarning')
    .controller('ChannelCtrl', function ($scope, $rootScope, $http, $state) {
        $scope.allChannels = [
            {_id: "mongo", level: 1},
            {_id: "mongo2", level: 2},
            {_id: "mongo3", level: 3}
        ];
        $scope.newChannel = {
            _id: "",
            level: "",
            note: ""
        };
        $scope.aChannel = {
            _id: "test-mongo",
            level: 10,
            note: "hehehe"
        };
        $scope.operationList = ['email', 'message', 'tel'];
        $scope.groupList = [];
        $scope.List = [];
        $scope.showPop = false;
        $scope.newChannelMessage = undefined;
        $scope.settingChannelMessage = undefined;
        $scope.setChannel = function (channel) {
            $scope.aChannel = channel;
            $scope.showPop = true;
        };
        $scope.submitSetChannel = function (channel) {
            $scope.settingChannelMessage = undefined;
            $http.post("/api/channels/setting", channel).success(function(data){
                if(data.status==1){
                    $scope.settingChannelMessage = "设置失败";
                }else{
                    $scope.settingChannelMessage = "channel 设置成功";
                }
            })
        };
        $scope.addChannel = function (channnel) {
            $scope.newChannelMessage = false;
            if (!channnel._id) {
                $scope.newChannelMessage = "请填写channel name";
                return;
            } else if (!channnel.level) {
                $scope.newChannelMessage = "请填写channel level";
                return;
            } else if (!channnel.note) {
                $scope.newChannelMessage = "请填写channel 备注";
                return;
            } else {
                $http.post("/api/channels", channnel).success(function (data) {
                    if (data.status == 1) {
                        $scope.newChannelMessage = "channel 添加成功!";
                        $scope.allChannels.push(channnel);
                    } else if (data.error) {
                        $scope.newChannelMessage = data.error;
                    } else {
                        $scope.newChannelMessage = "添加失败";
                    }
                });
            }
        };
        $scope.$watch('aChannel.level', function (newValue, oldValue) {
            if (newValue !== oldValue) {
                for (i = 1; i < newValue + 1; i++) {
                    var name = "level" + i;
                    if ($scope.aChannel.event) {
                        if (!$scope.aChannel.event[name]) {
                            $scope.aChannel.event[name] = {
                                operation: ['email'],
                                groups: [],
                                await: ""
                            };
                        }
                    } else {
                        $scope.aChannel['event'] = {};
                        $scope.aChannel['event'][name] = {
                            operation: ['email'],
                            groups: [],
                            await: ""
                        };
                    }
                }
            }
        });

        $scope.toggle = function (item, key) {
            var idx = $scope.aChannel.event[key]['operation'].indexOf(item);
            if (idx > -1) $scope.aChannel.event[key]['operation'].splice(idx, 1);
            else $scope.aChannel.event[key]['operation'].push(item);
        };
        $scope.toggleGroup = function (item, key) {
            var idx = $scope.aChannel.event[key]['groups'].indexOf(item);
            if (idx > -1) $scope.aChannel.event[key]['groups'].splice(idx, 1);
            else $scope.aChannel.event[key]['groups'].push(item);
        };
        $scope.exists = function (item, list) {
            return list.indexOf(item) > -1;
        };
        var init = function () {
            $http.get("/api/channels").success(function (data) {
                if (data.status == 1) {
                    $scope.allChannels = data.data;
                } else {
                    console.log("some err");
                }
            })
            $http.get("/api/groups").success(function(data){
                if (data.status == 1) {
                    $scope.List = data.data;
                    for (var i = 0 ; i < $scope.List.length ; i++){
                        $scope.groupList[i] = $scope.List[i]._id;
                    }
                }
            });
        };
        init();
    });