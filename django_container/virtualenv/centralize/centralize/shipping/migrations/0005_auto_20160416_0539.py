# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-16 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0004_auto_20160416_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('LA', "Lao People's Democratic Republic"), ('SM', 'San Marino'), ('LT', 'Lithuania'), ('PA', 'Panama'), ('NP', 'Nepal'), ('RU', 'Russian Federation'), ('LK', 'Sri Lanka'), ('UA', 'Ukraine'), ('CW', 'Curaçao'), ('AR', 'Argentina'), ('WF', 'Wallis and Futuna'), ('AM', 'Armenia'), ('QA', 'Qatar'), ('GD', 'Grenada'), ('CX', 'Christmas Island'), ('TJ', 'Tajikistan'), ('AD', 'Andorra'), ('BE', 'Belgium'), ('FJ', 'Fiji'), ('PY', 'Paraguay'), ('RE', 'Réunion'), ('KE', 'Kenya'), ('MM', 'Myanmar'), ('ID', 'Indonesia'), ('GP', 'Guadeloupe'), ('IM', 'Isle of Man'), ('GA', 'Gabon'), ('AU', 'Australia'), ('MS', 'Montserrat'), ('GY', 'Guyana'), ('VC', 'Saint Vincent and the Grenadines'), ('VG', 'Virgin Islands (British)'), ('ST', 'Sao Tome and Principe'), ('TO', 'Tonga'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('BM', 'Bermuda'), ('AG', 'Antigua and Barbuda'), ('TM', 'Turkmenistan'), ('SB', 'Solomon Islands'), ('AT', 'Austria'), ('IL', 'Israel'), ('NO', 'Norway'), ('GU', 'Guam'), ('CO', 'Colombia'), ('YT', 'Mayotte'), ('TH', 'Thailand'), ('CU', 'Cuba'), ('SD', 'Sudan'), ('AF', 'Afghanistan'), ('CC', 'Cocos (Keeling) Islands'), ('PG', 'Papua New Guinea'), ('MP', 'Northern Mariana Islands'), ('MA', 'Morocco'), ('PW', 'Palau'), ('VI', 'Virgin Islands (U.S.)'), ('ET', 'Ethiopia'), ('CK', 'Cook Islands'), ('GG', 'Guernsey'), ('GT', 'Guatemala'), ('BS', 'Bahamas'), ('ML', 'Mali'), ('MC', 'Monaco'), ('EE', 'Estonia'), ('NU', 'Niue'), ('CD', 'Congo (the Democratic Republic of the)'), ('SV', 'El Salvador'), ('BZ', 'Belize'), ('KN', 'Saint Kitts and Nevis'), ('GM', 'Gambia'), ('CM', 'Cameroon'), ('BW', 'Botswana'), ('CA', 'Canada'), ('AS', 'American Samoa'), ('AO', 'Angola'), ('SJ', 'Svalbard and Jan Mayen'), ('BL', 'Saint Barthélemy'), ('BA', 'Bosnia and Herzegovina'), ('CL', 'Chile'), ('PF', 'French Polynesia'), ('GH', 'Ghana'), ('TC', 'Turks and Caicos Islands'), ('MX', 'Mexico'), ('BR', 'Brazil'), ('WS', 'Samoa'), ('AE', 'United Arab Emirates'), ('SE', 'Sweden'), ('SK', 'Slovakia'), ('TD', 'Chad'), ('KR', 'Korea (the Republic of)'), ('BO', 'Bolivia (Plurinational State of)'), ('ZM', 'Zambia'), ('KG', 'Kyrgyzstan'), ('JM', 'Jamaica'), ('IN', 'India'), ('MH', 'Marshall Islands'), ('MZ', 'Mozambique'), ('BJ', 'Benin'), ('NE', 'Niger'), ('DK', 'Denmark'), ('AZ', 'Azerbaijan'), ('JO', 'Jordan'), ('LY', 'Libya'), ('IQ', 'Iraq'), ('PR', 'Puerto Rico'), ('JP', 'Japan'), ('PE', 'Peru'), ('SY', 'Syrian Arab Republic'), ('CF', 'Central African Republic'), ('BY', 'Belarus'), ('MQ', 'Martinique'), ('MO', 'Macao'), ('GF', 'French Guiana'), ('BN', 'Brunei Darussalam'), ('TW', 'Taiwan (Province of China)'), ('TV', 'Tuvalu'), ('VN', 'Viet Nam'), ('GI', 'Gibraltar'), ('TZ', 'Tanzania, United Republic of'), ('TG', 'Togo'), ('KH', 'Cambodia'), ('ER', 'Eritrea'), ('VU', 'Vanuatu'), ('UG', 'Uganda'), ('KM', 'Comoros'), ('AW', 'Aruba'), ('LU', 'Luxembourg'), ('LB', 'Lebanon'), ('GQ', 'Equatorial Guinea'), ('GW', 'Guinea-Bissau'), ('FR', 'France'), ('DZ', 'Algeria'), ('HM', 'Heard Island and McDonald Islands'), ('MN', 'Mongolia'), ('BH', 'Bahrain'), ('SC', 'Seychelles'), ('AQ', 'Antarctica'), ('PH', 'Philippines'), ('RS', 'Serbia'), ('MR', 'Mauritania'), ('DE', 'Germany'), ('CZ', 'Czech Republic'), ('ZA', 'South Africa'), ('AX', 'Åland Islands'), ('UY', 'Uruguay'), ('NG', 'Nigeria'), ('OM', 'Oman'), ('ES', 'Spain'), ('CY', 'Cyprus'), ('LI', 'Liechtenstein'), ('NA', 'Namibia'), ('CI', "Côte d'Ivoire"), ('KI', 'Kiribati'), ('MU', 'Mauritius'), ('KW', 'Kuwait'), ('KZ', 'Kazakhstan'), ('BG', 'Bulgaria'), ('PK', 'Pakistan'), ('LC', 'Saint Lucia'), ('JE', 'Jersey'), ('HR', 'Croatia'), ('IR', 'Iran (Islamic Republic of)'), ('PT', 'Portugal'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('CR', 'Costa Rica'), ('SA', 'Saudi Arabia'), ('IO', 'British Indian Ocean Territory'), ('BD', 'Bangladesh'), ('GR', 'Greece'), ('VA', 'Holy See'), ('SS', 'South Sudan'), ('SL', 'Sierra Leone'), ('BT', 'Bhutan'), ('MF', 'Saint Martin (French part)'), ('CN', 'China'), ('GN', 'Guinea'), ('MW', 'Malawi'), ('PM', 'Saint Pierre and Miquelon'), ('BF', 'Burkina Faso'), ('MT', 'Malta'), ('PS', 'Palestine, State of'), ('NC', 'New Caledonia'), ('NR', 'Nauru'), ('NL', 'Netherlands'), ('BV', 'Bouvet Island'), ('KP', "Korea (the Democratic People's Republic of)"), ('SN', 'Senegal'), ('LV', 'Latvia'), ('GL', 'Greenland'), ('PL', 'Poland'), ('FM', 'Micronesia (Federated States of)'), ('RW', 'Rwanda'), ('LS', 'Lesotho'), ('CH', 'Switzerland'), ('MG', 'Madagascar'), ('NF', 'Norfolk Island'), ('EG', 'Egypt'), ('HN', 'Honduras'), ('UM', 'United States Minor Outlying Islands'), ('LR', 'Liberia'), ('RO', 'Romania'), ('UZ', 'Uzbekistan'), ('MD', 'Moldova (the Republic of)'), ('SO', 'Somalia'), ('IS', 'Iceland'), ('IT', 'Italy'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('DJ', 'Djibouti'), ('AI', 'Anguilla'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('DO', 'Dominican Republic'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('YE', 'Yemen'), ('FO', 'Faroe Islands'), ('GS', 'South Georgia and the South Sandwich Islands'), ('DM', 'Dominica'), ('MV', 'Maldives'), ('ME', 'Montenegro'), ('HU', 'Hungary'), ('FI', 'Finland'), ('AL', 'Albania'), ('TL', 'Timor-Leste'), ('TK', 'Tokelau'), ('TR', 'Turkey'), ('BB', 'Barbados'), ('BI', 'Burundi'), ('KY', 'Cayman Islands'), ('EC', 'Ecuador'), ('PN', 'Pitcairn'), ('HK', 'Hong Kong'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('FK', 'Falkland Islands  [Malvinas]'), ('CG', 'Congo'), ('TF', 'French Southern Territories'), ('MY', 'Malaysia'), ('SR', 'Suriname'), ('NI', 'Nicaragua'), ('SI', 'Slovenia'), ('IE', 'Ireland'), ('GE', 'Georgia'), ('HT', 'Haiti'), ('EH', 'Western Sahara'), ('NZ', 'New Zealand'), ('TN', 'Tunisia'), ('ZW', 'Zimbabwe'), ('TT', 'Trinidad and Tobago'), ('CV', 'Cabo Verde'), ('US', 'United States of America'), ('SZ', 'Swaziland')], default='', max_length=2),
        ),
    ]
