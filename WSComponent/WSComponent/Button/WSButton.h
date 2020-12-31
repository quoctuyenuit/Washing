//
//  WSButton.h
//  WSComponent
//
//  Created by Quốc Tuyến on 11/23/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "WSGradientData.h"

NS_ASSUME_NONNULL_BEGIN

@interface WSButton : UIButton

@property(nonatomic, strong) WSGradientData *gradientBackgroundColor;

@end

NS_ASSUME_NONNULL_END
