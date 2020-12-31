//
//  WSWindowManager.m
//  Washing
//
//  Created by Quốc Tuyến on 11/23/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import "WSWindowManager.h"

@interface WSWindowManager ()

@property(nonatomic, strong, readwrite) WSWindow *rootWindow;

@end

@implementation WSWindowManager

+ (WSWindowManager *)sharedWindow {
    static WSWindowManager *sharedWindow;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        sharedWindow = [[WSWindowManager alloc] init];
    });
    return sharedWindow;
}

- (WSWindow *)rootWindow {
    if (!_rootWindow) {
        _rootWindow = [[WSWindow alloc] initWithFrame:[UIScreen mainScreen].bounds];
    }
    return _rootWindow;
}

@end
