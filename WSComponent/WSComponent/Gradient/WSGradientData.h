//
//  WSGradientData.h
//  WSComponent
//
//  Created by Quốc Tuyến on 11/25/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

NS_ASSUME_NONNULL_BEGIN

@interface WSGradientData : NSObject

@property(nonatomic, assign) CGPoint startPoint;

@property(nonatomic, assign) CGPoint endPoint;

@property(nonatomic, strong) NSArray *colors;

- (instancetype)initWithColors:(NSArray<UIColor *> *)colors
                    startPoint:(CGPoint)startPoint
                      endPoint:(CGPoint)endPoint;

@end

NS_ASSUME_NONNULL_END
