//
//  WSElementColors.m
//  Washing
//
//  Created by Quốc Tuyến on 12/2/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import "WSElementColors.h"
#import "WSColorPalettes.h"
#import "WSElementColors+Private.h"
#import "ColorJsonified.h"

@interface WSElementColors ()

@property(nonatomic, strong, readwrite) WSColorPalettes *colorPalettes;

@end

@implementation WSElementColors

+ (WSElementColors *)shared {
    static WSElementColors *element;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        element = [[WSElementColors alloc] init];
    });
    return element;
}

- (instancetype)init
{
    self = [super init];
    if (self) {
        _colorPalettes = [[WSColorPalettes alloc] initWithJsonified:_ColorJsonified];
    }
    return self;
}

@end
