import fr from '../locales/fr.json';
import en from '../locales/en.json';
import ar from '../locales/ar.json';

const translations: Record<string, Record<string, any>> = { fr, en, ar };

export function useTranslations(lang: string = 'fr') {
  return function t(key: string): string {
    const keys = key.split('.');
    let current: any = translations[lang] || translations['fr'];
    for (const k of keys) {
      if (current && typeof current === 'object' && k in current) {
        current = current[k];
      } else {
        return key;
      }
    }
    return typeof current === 'string' ? current : key;
  };
}
